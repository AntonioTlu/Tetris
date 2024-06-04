import pygame, sys
from game import Game
from colors import Colors
from database import Database
from scoreboard import Scoreboard


# Initialise Database
db = Database()
connection = db.create_connection(db.path)
db.execute_query(connection, db.create_score_table)


# Initialise Game
pygame.init()

# Styling the font
title_font = pygame.font.Font(None, 40)
# Creating all the start surfaces
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
start_button_surface = title_font.render("Start", True, Colors.white)
scoreboard_button_surface = title_font.render("Scores", True, Colors.white)
# Creating all the start rects
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 185, 170, 180)
start_rect = pygame.Rect(320, 450, 170, 60)
scoreboard_rect = pygame.Rect(320, 530, 170, 60)

# Setting up the screen
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

# Initialise Clock, Game and Scoreboard
clock = pygame.time.Clock()
game = Game()
scoreboard = Scoreboard()

# Interval is the starting speed of the falling blocks. Lower value -> blocks fall faster
interval = 300

# Initialise the Game updates while runtime
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, interval)

# Variables for the Game loop
width = screen.get_width()
height = screen.get_height()
# Variable used in Game loop for interval reduction
previous_cleared_lines = 0
# Save flag used in Game loop for Restart Game Button
only_save_once = 0


### GAME LOOP ###
while True:
    # Getting mouse position to check later on if buttons were clicked
    mouse = pygame.mouse.get_pos()

    # Event Handling
    for event in pygame.event.get():
        # Quit the Game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for Key inputs
        if event.type == pygame.KEYDOWN:
            # Left
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            # Right
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            # Down
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                # For every Down press player gain +1 Point
                game.update_score(0, 1)
            # Rotate Block
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            # Hard Drop
            if event.key == pygame.K_SPACE and game.game_over == False:
                points = game.move_to_bottom()
                # For every Hard Drop the Player gains double the points
                game.update_score(0, points * 2)
        # Moves the Blocks Down while Game running
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        # Checks if mouse clicked on Start button when Game is over
        if event.type == pygame.MOUSEBUTTONDOWN and game.game_over == True:
            if 320 <= mouse[0] <= 490 and 450 <= mouse[1] <= 510:
                game.game_over = False
                only_save_once = 0
                game.reset()
        # Go to Highscore Screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 320 <= mouse[0] <= 490 and 530 <= mouse[1] <= 590:
                scoreboard.show_highscore_screen(screen, width, connection)

    # Increases the Game speed per 10 cleared lines
    cleared_lines = game.get_cleared_line()
    # Max game speed is 60ms between next down movement of Block
    if interval > 60:
        if cleared_lines > previous_cleared_lines:
            previous_cleared_lines = cleared_lines
            if cleared_lines % 10 == 0:
                interval -= 20
                pygame.time.set_timer(GAME_UPDATE, interval)

    # creating the Score Value Surface
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    # setting up the items on Screen and giving it color
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 150, 50, 50))
    pygame.draw.rect(screen, Colors.light_blue, scoreboard_rect, 0, 10)
    screen.blit(scoreboard_button_surface, (360, 548, 50, 50))

    # Game Over Overlay
    if game.game_over == True:
        if only_save_once == 0:
            db.create_new_score(connection, game.score)
            only_save_once = 1
        screen.blit(game_over_surface, (320, 400, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, start_rect, 0, 10)
        screen.blit(start_button_surface, (370, 468, 50, 50))

    # Drawing the Score Value Rect + Surface
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    # Drawing the Screen
    game.draw(screen)

    # Updates the Game (set to 60FPS)
    pygame.display.update()
    clock.tick(60)
