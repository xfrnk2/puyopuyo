# 목표 : 클론 코딩을 하지 말고, staticmethod 선언을 하지 않고 만들어 보기
from event import EventManager, GameExitEvent
from field import Field
from logic import Logic
from puyo import CurrentPuyo, Puyo
from renderer import Renderer
from timer import Timer

WIDTH = 12
HEIGHT = 20


class Game:
    def __init__(self):
        Timer.init()
        self.__renderer = Renderer()
        self.__event = EventManager()
        self.__game_objects = {}
        self.__logic = Logic()
        self.__current_puyo = None
        self.__field = Field()

    def run(self):
        is_continue = self.__update()
        while is_continue:
            is_continue = self.__update()
            self.__render()

    def __update(self):
        Timer.capture_time()
        current_event = self.__event.get_event()
        if isinstance(current_event, GameExitEvent):
            return False

        self.__logic.update()
        self.__logic.set_game_objects(tuple(self.__game_objects.values()))

        if self.__current_puyo:
            self.__current_puyo.update(current_event)
        # for game_object in self.__game_objects.values():
        #     game_object.update(elapsed_time, current_event)

        current_puyo = self.__current_puyo

        if not current_puyo or not current_puyo.valid:
            PuyoA, PuyoB = Puyo(self.__logic), Puyo(self.__logic)
            PuyoA.position = (6, 19)

            new_puyo = CurrentPuyo(PuyoA, PuyoB)
            self.__game_objects[PuyoA.id] = PuyoA
            self.__game_objects[PuyoB.id] = PuyoB

            self.__current_puyo = new_puyo

        self.__field.update(tuple(self.__game_objects.values()))
        return True

    def __render(self):
        if self.__renderer.render_begin():
            self.__renderer.render(self.__field)
