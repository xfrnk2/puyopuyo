from uuid import uuid4

from src.event import Event, MoveLeftEvent, MoveRightEvent, MoveDownEvent, VoidEvent

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
    def position(self):
        return self.__x, self.__y

    @position.setter
    def position(self, coordinates: tuple):
        x, y = coordinates
        self.__x, self.__y = x, y

    def reflect_event(self, event: Event):
        if isinstance(event, VoidEvent):
            return self.position

        x, y = self.position
        if isinstance(event, MoveLeftEvent):
            x -= 1
        elif isinstance(event, MoveRightEvent):
            x += 1
        elif isinstance(event, MoveDownEvent):
            y += 1

        return x, y

    def falling(self, time):
        y = self.__y
        y -= self.__speed * time

        is_valid = int(y) < self.__y
        self.__y = y
        return is_valid

    def update(self, time, event):

        new_position = self.reflect_event(event)
        is_updatable = 'self.__logic.valid_coordinates(new_position) and not self.__logic.already_exist(self, new_position)'

        if eval(is_updatable):
            self.position = new_position

        if not self.falling(time):
            return

        new_position = (self.__x, int(self.__y))
        if not eval(is_updatable):
            self.__valid = False

        self.position = new_position
