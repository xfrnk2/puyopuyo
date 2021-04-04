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

    def update(self):
        self.__logic = copy.deepcopy(self.__original_logic)

    def set_game_objects(self, game_objects):
        for game_object in game_objects:
            x, y = game_object.position
            self.__logic[self.__height - y - 1][x] = game_object

    def already_exist(self, puyo, position):
        try:
            x, y = position
            y = int(y)
            return self.__logic[self.__height - y - 1][x] and self.__logic[self.__height - y - 1][x] != puyo
        except IndexError:
            pass

    def valid_coordinates(self, position):
        x, y = position
        y = int(y)
        return 0 <= y < self.__height and 0 <= x < self.__width

    def is_updatable(self, new_position):
        return self.valid_coordinates(new_position) and not self.already_exist(self, new_position)
