from dataclasses import dataclass

from src.event import Event, MoveDownEvent, MoveLeftEvent, MoveRightEvent
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


def test_event_reflect():
    logic = Logic()
    cases = (
        EventReflectCase(event=MoveLeftEvent, prev_position=(6, 5), expected=(5, 5)),
        EventReflectCase(event=MoveRightEvent, prev_position=(6, 6), expected=(7, 6)),
        EventReflectCase(event=MoveDownEvent, prev_position=(2, 15), expected=(2, 16))
    )

    for case in cases:
        event, prev_position, expected = case.event, case.prev_position, case.expected
        puyo = Puyo(logic)

        puyo.position = prev_position
        result = puyo.reflect_event(event())
        assert result == expected


def test_falling():
    logic = Logic()
    cases = (
        FallingCase(time=0.1, expected=True),
        FallingCase(time=0, expected=False)
    )

    for case in cases:
        time, expected = case.time, case.expected
        puyo = Puyo(logic)
        assert puyo.falling(time) == expected
