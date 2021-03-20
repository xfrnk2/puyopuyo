from event import Event
from game_object import GameObject


class Block(GameObject):
    def __init__(self):
        self.__data = '□'

    def __repr__(self):
        return self.__data

    def __str__(self):
        return self.__data

    def set(self, data):
        self.__data = data

    def update(self, event: Event):
        pass

    def render(self):
        pass
