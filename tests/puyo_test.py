from dataclasses import dataclass

from src.event import (Event, LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                       MoveRightEvent, RightSpinEvent)
from src.logic import Logic
from src.puyo import Puyo


@dataclass
class EventReflectCase:
    event: Event
    prev_position: tuple
    expected: tuple


def test_event_reflect():
    '''
    :조작 이벤트에 따라 변경된 좌표값을 정상적으로 리턴하는지 테스트:
    '''
    cases = (
        EventReflectCase(event=MoveLeftEvent, prev_position=(6, 5), expected=(5, 5)),
        EventReflectCase(event=MoveRightEvent, prev_position=(6, 6), expected=(7, 6)),
        EventReflectCase(event=MoveDownEvent, prev_position=(2, 15), expected=(2, 16)),
        EventReflectCase(event=LeftSpinEvent, prev_position=(5, 10), expected=(4, 11)),
        EventReflectCase(event=RightSpinEvent, prev_position=(5, 10), expected=(6, 11))
    )

    for case in cases:
        event, prev_position, expected = case.event, case.prev_position, case.expected
        puyo = Puyo(Logic())

        puyo.position = prev_position
        result = puyo.reflect_event(event())
        assert result == expected
