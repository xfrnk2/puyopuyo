from uuid import uuid4
import copy
from event import (Event, LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                   MoveRightEvent, RightSpinEvent, VoidEvent, SpinEvent, MoveEvent)
from logic import Logic
from timer import Timer
from enum import Enum

WIDTH = 12
HEIGHT = 20


class Direction(Enum):
    # 반시계방향(z회전) 변화값
    EAST = -1, 1
    WEST = 1, -1
    NORTH = -1, -1
    SOUTH = 1, 1

    # 시계방향(x회전) 이동시 위 일련의 값들로부터 곱할 값
    # EAST = 1, -1
    # WEST = 1, -1
    # NORTH = -1, 1
    # SOUTH = -1, 1


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

    def moving_update(self, event):
        target = self.__data[type(event)]

        adding_values = [0, 0]
        lower, upper = sorted([self.__main_puyo, self.__sub_puyo], key=lambda puyo: [puyo.y, puyo.x])
        add = lambda x, y: (x[0] + y[0], x[1] + y[1])
        pivot = lower
        if isinstance(event, MoveRightEvent):
            pivot = upper

        pivot_valid = pivot.is_updatable(add(pivot.position, target))
        valid = lower.is_updatable(add(lower.position, target)) and upper.is_updatable(add(upper.position, target))

        if lower.x == upper.x:
            if isinstance(event, MoveDownEvent):
                if pivot_valid:
                    adding_values = add(adding_values, target)
                else:
                    self.__valid = False
                    return
            elif valid:
                adding_values = add(adding_values, target)

        else:
            if isinstance(event, MoveDownEvent):
                if valid:
                    adding_values = add(adding_values, target)
                else:
                    self.__valid = False
                    return

            elif pivot_valid:
                adding_values = add(adding_values, target)

        lower.position = add(lower.position, adding_values)
        upper.position = add(upper.position, adding_values)
