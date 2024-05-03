import pygame
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
running = True

game = Game()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(DARK_BLUE)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
