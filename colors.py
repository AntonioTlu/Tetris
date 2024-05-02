class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (230, 23, 23)
    orange = (230, 126, 23)
    yellow = (230, 230, 23)
    purple = (126, 23, 230)
    cyan = (23, 230, 230)
    blue = (23, 23, 230)
    
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]