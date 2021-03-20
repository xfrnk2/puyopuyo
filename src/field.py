import copy
from uuid import uuid4

from Timer import timer

WIDTH=12
HEIGHT=20

class Field:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.__width = width
        self.__height = height
        self.__original_field = [['□'for _ in range(width)]for _ in range(height)]
        self.__field = None

    def render_puyo(self, position, data):
        x, y = position
        self.__field[self.__height - y - 1][x] = data

    def update(self, puyo_objects):
        self.__field = copy.deepcopy(self.__original_field)
        for puyo in puyo_objects:
            position, data = puyo.position, puyo.data
            render_puyo(position, data)
