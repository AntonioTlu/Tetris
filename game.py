import random
import pygame
from grid import Grid
from blocks import *


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.cleared_lines = 0

    ### FUNCTIONS ###
    def update_score(self, lines_cleared, move_down_points):
        """Update the score based on the number of lines cleared and the points gained from moving down.

        Args:
            - lines_cleared (int): The number of lines cleared.
            - move_down_points (int): The number of points gained from moving down.
        """

        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_cleared_line(self):
        """Get the number of lines cleared.
        return: (int) The number of lines cleared.
        """
        return self.cleared_lines

    def get_random_block(self):
        """Get a random block from the list of blocks.
        return: (Block) A random block.
        """
        if len(self.blocks) == 0:
            self.blocks = [
                IBlock(),
                JBlock(),
                LBlock(),
                OBlock(),
                SBlock(),
                TBlock(),
                ZBlock(),
            ]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        """moves block one space to the left"""
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            # undo move if block is outside the grid or collides with another block
            self.current_block.move(0, 1)

    def move_right(self):
        """moves block one space to the right"""
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            # undo move if block is outside the grid or collides with another block
            self.current_block.move(0, -1)

    def move_down(self):
        """moves block one space down"""
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            # undo move if block is outside the grid or collides with another block
            self.current_block.move(-1, 0)
            self.lock_block()

    def move_to_bottom(self):
        """moves block to the bottom of the grid and locks it in place
        return: (int) The number of points gained from moving the block to the bottom.
        """
        points = 0
        loop = True
        while loop:
            self.current_block.move(1, 0)
            # gain 1 point for every space moved down
            points += 1
            if self.block_inside() == False or self.block_fits() == False:
                # undo move if block is outside the grid or collides with another block
                self.current_block.move(-1, 0)
                self.lock_block()
                loop = False
        return points

    def lock_block(self):
        """locks the current block in place and checks for full rows to clear"""
        tiles = self.current_block.get_cell_positions()
        # update grid with block tiles
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # check for full rows
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.cleared_lines += rows_cleared
        # update score
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
        # check if the new block fits
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        """resets the game to the initial state"""
        self.grid.reset()
        self.blocks = [
            IBlock(),
            JBlock(),
            LBlock(),
            OBlock(),
            SBlock(),
            TBlock(),
            ZBlock(),
        ]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):
        """checks if the Block fits
        return: (bool) True if the block fits, False otherwise.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        """rotates the current block"""
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            # undo rotation if block is outside the grid or collides with another block
            self.current_block.undo_rotation()

    def block_inside(self):
        """checks if the block is inside the grid
        return: (bool) True if the block is inside the grid, False otherwise.
        """
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        """draws the game on the screen"""
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # draw the next block
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)
