import pygame
from colors import Colors
from game import Game

game = Game()


class Scoreboard:

    def show_highscore_screen(self, screen, width):
        running = True
        while running:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70:
                        return

            # Clear the screen
            screen.fill(Colors.dark_blue)

            # Draw the highscore screen
            # This is where you would draw your highscores
            # For now, let's just draw some text

            font = pygame.font.Font(None, 36)
            text = font.render("Highscore Screen", True, (255, 255, 255))
            screen.blit(text, (width // 2 - text.get_width() // 2, 20))

            font = pygame.font.Font(None, 48)
            back_button_surface = font.render("<", True, Colors.white)
            back_button_rect = pygame.Rect(20, 20, 50, 50)

            pygame.draw.rect(screen, Colors.light_blue, back_button_rect, 0, 10)
            screen.blit(back_button_surface, (33, 25, 50, 50))

            pygame.display.flip()

        pygame.quit()
