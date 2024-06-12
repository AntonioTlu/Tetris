from colors import Colors
import pygame
from position import Position


class Block:
    """
    Info:
    ----------------
    Class representing a block in the game.

    Attributes:
    ----------------
        - id (int): The id of the block.
        - cells (dict): A dictionary containing the cells of the block.
        - cell_size (int): The size of the cells in the block.
        - row_offset (int): The row offset of the block.
        - column_offset (int): The column offset of the block.
        - rotation_state (int): The rotation state of the block.
        - colors (dict): A dictionary containing the colors of the block.

    Methods:
    ----------------
        - move(rows, columns): Moves the block by the given amount of rows and columns.
        - get_cell_positions(): Returns the positions of the cells of the block.
        - rotate(): Rotates the block.
        - undo_rotation(): Undoes the rotation of the block.
        - draw(screen, offset_x, offset_y): Draws the block on the screen.
    """

    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    ### FUNCTIONS ###
    def move(self, rows, columns):
        """
        Info:
        ----------------
        Moves the block by the given amount of rows and columns.

        Args:
        ----------------
            - rows (int): The number of rows to move the block.
            - columns (int): The number of columns to move the block.
        """
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        """
        Info:
        ----------------
        Returns (list) the positions of the cells of the block."""
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(
                position.row + self.row_offset, position.column + self.column_offset
            )
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        """
        Info:
        ----------------
        Rotates the block."""
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        """
        Info:
        ----------------
        Undoes the rotation of the block."""
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        """
        Info:
        ----------------
        Draws the block on the screen.

        Args:
        ----------------
            - screen (pygame.Surface): The screen to draw the block on.
            - offset_x (int): The x-coordinate offset of the block.
            - offset_y (int): The y-coordinate offset of the block.
        """
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1,
            )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
