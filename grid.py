import pygame
from colors import Colors


class Grid:
    """
    Info:
    ----------------
    Grid class is a class that represents the game grid.

    Attributes:
    ----------------
        - num_rows (int): The number of rows in the grid.
        - num_cols (int): The number of columns in the grid.
        - cell_size (int): The size of the cells in the grid.
        - grid (list): A 2D list representing the grid.
        - colors (list): A list containing the colors of the grid cells.

    Methods:
    ----------------
        - print_grid(): Prints the grid to the console.
        - is_inside(row, column): Check if the given row and column are inside the grid.
        - is_empty(row, column): Check if the cell at the given row and column is empty.
        - is_row_full(row): Check if the given row is full.
        - clear_row(row): Clear the given row.
        - move_row_down(row, num_rows): Move the given row down by the given number of rows.
        - clear_full_rows(): Clear all full rows and move the rows above them down.
        - reset(): Reset the grid to be empty.
        - get_cols(): Get the number of columns in the grid.
        - draw(screen): Draw the grid on the screen.
    """

    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    ### FUNCTIONS ###
    def print_grid(self):
        """
        Info:
        ----------------
        Prints the grid to the console. 0 is an empty cell, 1 is a filled cell."""
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        """
        Info:
        ----------------
        Check if the given row and column are inside the grid.

        Returns:
        ----------------
            - (bool) True if they are, False otherwise.

        Args:
        ----------------
            - row (int): The row to check.
            - column (int): The column to check.
        """
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self, row, column):
        """
        Info:
        ----------------
        Check if the cell at the given row and column is empty.

        Returns:
        ----------------
            - (bool) True if it is, False otherwise.

        Args:
        ----------------
            - row (int): The row to check.
            - column (int): The column to check.
        """
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        """
        Info:
        ----------------
        Check if the given row is full.

        Returns:
        ---------------
            - (bool) True if it is, False otherwise.

        Args:
        ---------------
            - row (int): The row to check.
        """
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        """
        Info:
        ----------------
        Clear the given row.

        Args:
        ----------------
            - row (int): The row to clear.
        """
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        """
        Info:
        ----------------
        Move the given row down by the given number of rows.

        Args:
        ----------------
            - row (int): The row to move.
            - num_rows (int): The number of rows to move.
        """
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clear_full_rows(self):
        """
        Info:
        ----------------
        Clear all full rows and move the rows above them down.

        Returns:
        ----------------
            - (int) The number of rows cleared.
        """
        completed = 0
        for row in range(self.num_rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        """
        Info:
        ----------------
        Reset the grid to be empty."""
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def get_cols(self):
        """
        Info:
        ----------------
        Get the number of columns in the grid.

        Returns:
        ----------------
            - (int) The number of columns."""
        return self.num_cols

    def draw(self, screen):
        """
        Info:
        ----------------
        Draw the grid on the screen.

        Args:
        ----------------
            - screen (pygame.Surface): The screen to draw the grid on.
        """
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 11,
                    row * self.cell_size + 11,
                    self.cell_size - 1,
                    self.cell_size - 1,
                )
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
