from uuid import uuid4

from src.event import MoveDownEvent, MoveLeftEvent, MoveRightEvent, VoidEvent, LeftSpinEvent, RightSpinEvent

WIDTH = 12
HEIGHT = 20


class Puyo:
    def __init__(self, logic, width=WIDTH, height=HEIGHT):
        self.__id = uuid4()
        self.__x = width // 2
        self.__y = height

        self.__valid = True
        self.__speed = 1

        self.__logic = logic

    @property
    def valid(self):
        return self.__valid

    @property
    def position(self):
        return self.__x, self.__y

    @position.setter
    def position(self, coordinates):
        x, y = coordinates
        self.__x, self.__y = x, y
