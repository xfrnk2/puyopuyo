from uuid import uuid4
import copy
from event import (LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                       MoveRightEvent, RightSpinEvent, VoidEvent)
from logic import Logic
from timer import Timer

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

    def reflect_event(self, event):
        if isinstance(event, VoidEvent):
            return
        x, y = self.__x, self.__y

        if isinstance(event, MoveLeftEvent):
            x -= 1
        elif isinstance(event, MoveRightEvent):
            x += 1
        elif isinstance(event, MoveDownEvent):
            y -= 1
        if isinstance(event, LeftSpinEvent):
            x -= 1
            y -= 1
        elif isinstance(event, RightSpinEvent):
            x += 1
            y -= 1

        return x, y


    def update(self, time, event):
        if not self.valid:
            return

        new_position = self.reflect_event(event)
        is_updatable = 'self.logic.valid_coordinates(new_position) and ' \
                       'not self.logic.already_exist(self, new_position)'

        if new_position and eval(is_updatable):
            self.position = new_position

        y = self.__y
        y -= self.__speed * Timer.get_elapsed()
        y = max(y, 0)

        new_position = (self.__x, int(y))
        if not eval(is_updatable):
            self.valid = False
            return

        self.__y = y
        if int(self.__y) == 0:
            self.valid = False
