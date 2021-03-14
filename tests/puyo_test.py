from dataclasses import dataclass

from src.event import Event, MoveDownEvent, MoveLeftEvent, MoveRightEvent
from src.puyo import Puyo


@dataclass
class PuyoUpdateCase:
    time: float
    event: Event
    prev_position = tuple
    expected: tuple


class PuyoMock(Puyo):
    def __init__(self, position):
        x, y = position
        self._x = x
        self._y = y


def test_puyo_update():
    cases = (PuyoUpdateCase(time=0.01, event=MoveLeftEvent, prev_position=(6, 20), expected=(5, 20)),
             PuyoUpdateCase(time=1.1, event=MoveRightEvent, prev_position=(6, 20), expected=(7, 19)),
             PuyoUpdateCase(time=1.1, event=MoveDownEvent, prev_position=(2, 15), expected=(2, 13)),
             PuyoUpdateCase(time=0.1, event=MoveDownEvent, prev_position=(2, 15), expected=(2, 14)),
             )
    for case in cases:
        puyo = PuyoMock(case.prev_position)
        puyo.update(case.time, case.event)
        assert puyo.position == case.expected
