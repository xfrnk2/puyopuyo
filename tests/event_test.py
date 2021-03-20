from dataclasses import dataclass

import pyautogui

from src.event import (Event, EventManager, GameExitEvent, LeftSpinEvent,
                       MoveLeftEvent, MoveRightEvent, RightSpinEvent,
                       VoidEvent)


@dataclass
class GetEventCase:
    key: str
    expected: Event


def test_event_manager():
    cases = (GetEventCase(key='z', expected=LeftSpinEvent),
             GetEventCase(key='left', expected=MoveLeftEvent),
             GetEventCase(key='right', expected=MoveRightEvent),
             GetEventCase(key='esc', expected=GameExitEvent),
             GetEventCase(key='x', expected=RightSpinEvent),
             GetEventCase(key='space', expected=VoidEvent))

    manager = EventManager()

    for case in cases:
        pyautogui.press(case.key)
        a = manager.get_event()
        assert isinstance(a, case.expected), '입력값에 맞는 Event를 리턴'
