import copy

from block import Block

WIDTH = 12
HEIGHT = 20


class Field:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.__width = width
        self.__height = height
        self.__original_field = [[Block() for _ in range(width)] for _ in range(height)]
        self.__field = None

    def update(self, puyo_objects):
        self.__field = copy.deepcopy(self.__original_field)
        for puyo in puyo_objects:
            try:
                x, y = puyo.position
                data = puyo.data
                self.__field[self.__height - y - 1][x].set(data)
            except IndexError:
                pass

    def render(self):
        for line in self.__field:
            output = ''
            for block in line:
                output += str(block)
            print(output)
