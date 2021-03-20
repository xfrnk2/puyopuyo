from dataclasses import dataclass

from src.event import (Event, LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                       MoveRightEvent, RightSpinEvent, VoidEvent)
from src.logic import Logic
from src.puyo import Puyo


@dataclass
class EventReflectCase:
    event: Event
    prev_position: tuple
    expected: tuple


@dataclass
class FallingCase:
    time: float
    expected: bool


@dataclass
class UpdateCase:
    prev_position: tuple
    time: float
    event: Event
    expected: tuple


def test_event_reflect():
    '''
    :조작 이벤트에 따라 변경된 좌표값을 정상적으로 리턴하는지 테스트:
    '''
    cases = (
        EventReflectCase(event=MoveLeftEvent, prev_position=(6, 5), expected=(5, 5)),
        EventReflectCase(event=MoveRightEvent, prev_position=(6, 6), expected=(7, 6)),
        EventReflectCase(event=MoveDownEvent, prev_position=(2, 15), expected=(2, 14)),
        EventReflectCase(event=LeftSpinEvent, prev_position=(5, 10), expected=(4, 9)),
        EventReflectCase(event=RightSpinEvent, prev_position=(5, 10), expected=(6, 9))
    )

    for case in cases:
        event, prev_position, expected = case.event, case.prev_position, case.expected
        puyo = Puyo(Logic())

        puyo.position = prev_position
        result = puyo.reflect_event(event())
        assert result == expected


def test_falling():
    '''
    :시간 경과에 따라 정상 낙하하는지 테스트:
    '''
    cases = (
        FallingCase(time=0.1, expected=True),
        FallingCase(time=0, expected=False)
    )

    for case in cases:
        time, expected = case.time, case.expected
        puyo = Puyo(Logic())
        assert puyo.falling(time) == expected


def test_update():
    '''
    :경과시간과 조작 이벤트에 따라 좌표값을 잘 반영하는지 테스트:
    '''
    cases = (UpdateCase(prev_position=(6, 5), time=0.1, event=LeftSpinEvent, expected=(5, 3)),
             UpdateCase(prev_position=(3, 3), time=0.0, event=MoveDownEvent, expected=(3, 2)),
             UpdateCase(prev_position=(7, 5), time=0.3, event=MoveRightEvent, expected=(8, 4)),
             UpdateCase(prev_position=(2, 19), time=0.2, event=RightSpinEvent, expected=(3, 17)),
             UpdateCase(prev_position=(3, 0), time=0.2, event=RightSpinEvent, expected=(3, 0)),
             UpdateCase(prev_position=(0, 0), time=0.2, event=VoidEvent, expected=(0, 0))
             )

    for case in cases:
        logic = Logic()
        logic.update({})
        puyo = Puyo(logic)
        puyo.position = case.prev_position
        print(puyo.position)
        puyo.update(case.time, case.event())
        print(puyo.position)
        assert puyo.position == case.expected
