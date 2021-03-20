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

    def reflect_event(self, event):
        if isinstance(event, VoidEvent):
            return self.position

        x, y = self.position
        if isinstance(event, MoveLeftEvent):
            x -= 1
        elif isinstance(event, MoveRightEvent):
            x += 1
        elif isinstance(event, MoveDownEvent):
            y += 1
        elif isinstance(event, LeftSpinEvent):
            x -= 1
            y += 1
        elif isinstance(event, RightSpinEvent):
            x += 1
            y += 1

        return x, y
