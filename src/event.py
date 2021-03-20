from abc import ABC

from pynput.keyboard import Key, KeyCode, Listener


class Event(ABC):
    pass


class GameExitEvent(Event):
    pass


class MoveLeftEvent(Event):
    pass


class MoveRightEvent(Event):
    pass


class MoveDownEvent(Event):
    pass


class LeftSpinEvent(Event):
    pass


class RightSpinEvent(Event):
    pass


class RoundEvent(Event):
    pass

class VoidEvent(Event):
    pass


class EventManager:

    def __init__(self):
        self.__listener = Listener(on_release=__class__.on_release)
        self.__listener.start()

    @staticmethod
    def on_release(key):
        __class__.__current_key = key

    @staticmethod
    def get_event() -> Event:
        handlers = {
            Key.left: MoveLeftEvent,
            Key.right: MoveRightEvent,
            Key.down: MoveDownEvent,
            Key.esc: GameExitEvent,
            KeyCode(char='z'): LeftSpinEvent,
            KeyCode(char='x'): RightSpinEvent
        }

        try:
            current_key = __class__.__current_key
            __class__.__current_key = None
            return handlers[current_key]()
        except KeyError:
            return VoidEvent()

    __current_key = None
