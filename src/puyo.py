from uuid import uuid4
import copy
from event import (Event, LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                   MoveRightEvent, RightSpinEvent, VoidEvent, SpinEvent, MoveEvent)
from logic import Logic
from timer import Timer
from enum import Enum

WIDTH = 12
HEIGHT = 20


class Puyo:
    def __init__(self, logic, width=WIDTH, height=HEIGHT):
        self.__id = uuid4()
        self.__x = width // 2
        self.__y = height
        self.__data = '◎'
        self.__valid = True
        self.__speed = 1

        self.__logic: Logic = logic

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @property
    def logic(self):
        return self.__logic

    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, value):
        self.__valid = value

    @property
    def position(self):
        return int(self.__x), int(self.__y)

    @position.setter
    def position(self, coordinates):
        x, y = coordinates
        self.__x, self.__y = x, y

    def falling(self):
        self.__y -= 1

    def is_updatable(self, new_position):
        return self.logic.valid_coordinates(new_position) and not self.logic.already_exist(self, new_position)


class CurrentPuyo:

    def __init__(self, a, b):
        self.__main_puyo = a
        self.__sub_puyo = b
        self.__tick = 1.0
        self.__valid = True
        self.__speed = 1
        self.__data = {MoveDownEvent: (0, -1), MoveLeftEvent: (-1, 0), MoveRightEvent: (1, 0)}

    @property
    def main_puyo(self):
        return self.__main_puyo

    @property
    def sub_puyo(self):
        return self.__sub_puyo
