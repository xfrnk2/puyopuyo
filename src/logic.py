import copy

WIDTH = 12
HEIGHT = 20


class Logic:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.__width = width
        self.__height = height
        self.__original_logic = [[None for _ in range(width)] for _ in range(height)]
        self.__logic = None

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def update(self, puyo_objects):
        self.__logic = copy.deepcopy(self.__original_logic)
        for puyo in puyo_objects:
            x, y = puyo.position
            self.__logic[self.__height - y - 1][x] = puyo

    def already_exist(self, puyo, position):
        try:
            x, y = puyo.position
            return self.__logic[self.__height - y - 1][x] and self.__logic[self.__height - y - 1][x] != puyo
        except IndexError:
            pass

    def valid_coordinates(self, position):
        x, y = position
        return 0 <= y < self.__height and 0 <= x < self.__width
