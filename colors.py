class Colors:
    """
    Info:
    ----------------
    Colors class is a class that contains the colors of the game.

    Attributes:
    ----------------
        - dark_grey (tuple): The dark grey color.
        - green (tuple): The green color.
        - red (tuple): The red color.
        - orange (tuple): The orange color.
        - yellow (tuple): The yellow color.
        - purple (tuple): The purple color.
        - cyan (tuple): The cyan color.
        - blue (tuple): The blue color.
        - white (tuple): The white color.
        - dark_blue (tuple): The dark blue color.
        - light_blue (tuple): The light blue color.

    Methods:
    ----------------
        - get_cell_colors(): Returns the cell colors of the game.
    """

    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        """
        Info:
        ----------------
        Returns (list) the cell colors of the game."""
        return [
            cls.dark_grey,
            cls.green,
            cls.red,
            cls.orange,
            cls.yellow,
            cls.purple,
            cls.cyan,
            cls.blue,
        ]
