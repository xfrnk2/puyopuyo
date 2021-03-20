from uuid import uuid4

from src.event import (LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                       MoveRightEvent, RightSpinEvent, VoidEvent)
from src.logic import Logic

WIDTH = 12
HEIGHT = 20


class Puyo:
    def __init__(self, logic, width=WIDTH, height=HEIGHT):
        self.__id = uuid4()
        self.__x = width // 2
        self.__y = height

        self.__valid = True
        self.__speed = 1

        self.__logic: Logic = logic

    @property
    def logic(self):
        return self.__logic

    @property
    def valid(self):
        return self.__valid

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

    def falling(self, time):
        y = self.__y
        y -= self.__speed * time

        is_valid = int(y) < self.__y
        self.__y = y
        return is_valid

    def update(self, time, event):

        if not self.valid:
            return

        new_position = self.reflect_event(event)
        is_updatable = 'self.logic.valid_coordinates(new_position) and ' \
                       'not self.logic.already_exist(self, new_position)'

        if new_position and eval(is_updatable):
            self.position = new_position

        if not self.falling(time):
            return

        new_position = self.__x, int(self.__y)
        if eval(is_updatable):
            self.position = new_position
            return

        self.__y = 0
        self.__valid = False
