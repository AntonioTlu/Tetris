import pygame, sys
from game import Game

# important variables
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
DARK_BLUE = (44, 44, 127)

# pygame setup
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game = Game()

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            if event.key == pygame.K_RIGHT:
                game.move_right()
            if event.key == pygame.K_DOWN:
                game.move_down()
            if event.key == pygame.K_UP:
                game.rotate()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
