import copy
import os
from time import time
from typing import TypedDict
from uuid import uuid4

from event import EventManager, GameExitEvent
from field import LogicField, RenderField
from renderer import Renderer
from timer import Timer

# 목표 : 클론 코딩을 하지 말고, staticmethod 선언을 하지 않고 만들어 보기
WIDTH = 6
HEIGHT = 12


class Game:
    def __init__(self):
        Timer.init()
        self.__renderer = Renderer()
        self.__logic = LogicField()
        self.__event = EventManager()

    def run(self):
        is_running = True
        while is_running:
            is_running = self.__update()
            self.__render()

    def __update(self):
        Timer.capture_time()

        # current_event = self.__event.get_event()
        # if isinstance(current_event, GameExitEvent):
        #     return False
        #
        # self.__logic.update(current_event)
        return True

    def __render(self):
        # field = self.__logic.renderer
        # self.__renderer.update(field)
        self.__renderer.render()
