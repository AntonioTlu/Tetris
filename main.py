import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
start_button_surface = title_font.render("Start", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)
start_rect = pygame.Rect(320, 500, 170, 60)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

interval = 300

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, interval)

width = screen.get_width()
height = screen.get_height()

previous_cleared_lines = 0

while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
        if event.type == pygame.MOUSEBUTTONDOWN and game.game_over == True:
            if 320 <= mouse[0] <= 490 and 500 <= mouse[1] <= 560:
                game.reset()
                game.game_over = False

    cleared_lines = game.get_cleared_line()
    if interval > 60:
        if cleared_lines > previous_cleared_lines:
            previous_cleared_lines = cleared_lines
            if cleared_lines % 10 == 0:
                print(cleared_lines)
                interval -= 20
                pygame.time.set_timer(GAME_UPDATE, interval)

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
        pygame.draw.rect(screen, Colors.light_blue, start_rect, 0, 10)
        screen.blit(start_button_surface, (370, 518, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(
        score_value_surface,
        score_value_surface.get_rect(
            centerx=score_rect.centerx, centery=score_rect.centery
        ),
    )
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)
