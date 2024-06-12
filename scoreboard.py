import pygame
from datetime import datetime
from colors import Colors
from game import Game
from database import Database


# Initialise Game and Database
game = Game()
db = Database()


class Scoreboard:
    """
    Info:
    ----------------
    Class to display the highscore screen.

    Methods:
    ----------------
        - show_highscore_screen(screen, width, connection): Show the highscore screen with the top 10 scores.
    """

    def show_highscore_screen(self, screen, width, connection):
        """
        Info:
        ----------------
        Show the highscore screen with the top 10 scores.

        Args:
        ----------------
            - screen (pygame.Surface): The screen to display the highscore screen on.
            - width (int): The width of the screen.
            - connection (sqlite3.Connection): The connection to the database.

        """

        # Flags
        running = True
        read_once = 0

        # Scoreboard loop
        while running:

            # Get the mouse position
            mouse = pygame.mouse.get_pos()

            # Event Handling
            for event in pygame.event.get():
                # Quit the game
                if event.type == pygame.QUIT:
                    running = False
                # Go back to the main menu
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 20 <= mouse[0] <= 70 and 20 <= mouse[1] <= 70:
                        return

            # Clear the screen
            screen.fill(Colors.dark_blue)

            # Draw the highscore screen
            if read_once == 0:
                score_list = db.execute_read_query(connection)
                read_once = 1

            # Render each score and blit it on the screen
            vertical_offset = 20
            score_font = pygame.font.Font(None, 24)
            for i, score in enumerate(score_list):
                # Convert the score to a string, remove brackets and quotes, and split the values
                score_str = (
                    str(score).replace("(", "").replace(")", "").replace("'", "")
                )
                _, date, points = score_str.split(", ")

                # Convert the date format from 'YYYY-MM-DD' to 'DD.MM.YYYY'
                date = datetime.strptime(date, "%Y-%m-%d").strftime("%d.%m.%Y")

                # Render and blit the rank, date, and points
                rank_text = score_font.render(str(i + 1), True, (255, 255, 255))
                date_text = score_font.render(date, True, (255, 255, 255))
                points_text = score_font.render(points, True, (255, 255, 255))

                screen.blit(
                    rank_text,
                    (
                        width // 4 - rank_text.get_width() // 2,
                        60 + vertical_offset + i * 30,
                    ),
                )
                screen.blit(
                    date_text,
                    (
                        width // 2 - date_text.get_width() // 2,
                        60 + vertical_offset + i * 30,
                    ),
                )
                screen.blit(
                    points_text,
                    (
                        3 * width // 4 - points_text.get_width() // 2,
                        60 + vertical_offset + i * 30,
                    ),
                )

            # Draw the back button
            font = pygame.font.Font(None, 48)
            back_button_surface = font.render("<", True, Colors.white)
            back_button_rect = pygame.Rect(20, 20, 50, 50)

            pygame.draw.rect(screen, Colors.light_blue, back_button_rect, 0, 10)
            screen.blit(back_button_surface, (33, 25, 50, 50))

            # Display the highscore screen
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
