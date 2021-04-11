import sys
from dataclasses import dataclass

from src.event import (Event, LeftSpinEvent, MoveDownEvent, MoveLeftEvent,
                       MoveRightEvent, RightSpinEvent)
from src.logic import Logic
from src.puyo import CurrentPuyo, Puyo

sys.path.append('C:/Users/rad87/Documents/programming/puyopuyo')


@dataclass
class UpdateCase:
    event: Event
    prev_position: tuple
    expected_position: tuple


def test_moving_update():
    '''
    좌우 배치, 상하 배치, 방향별 벽면을 마주하고 event 발생시 (좌우배치 -> 상하배치 -> 상하반전배치 순)로 총 5회 테스트
    '''
    cases = (
        UpdateCase(event=MoveLeftEvent, prev_position=((4, 7), (5, 7)), expected_position=((3, 7), (4, 7))),
        UpdateCase(event=MoveLeftEvent, prev_position=((5, 5), (5, 4)), expected_position=((4, 5), (4, 4))),
        UpdateCase(event=MoveLeftEvent, prev_position=((0, 2), (1, 2)), expected_position=((0, 2), (1, 2))),
        UpdateCase(event=MoveLeftEvent, prev_position=((0, 0), (0, 1)), expected_position=((0, 0), (0, 1))),
        UpdateCase(event=MoveLeftEvent, prev_position=((0, 1), (0, 0)), expected_position=((0, 1), (0, 0))),

        UpdateCase(event=MoveRightEvent, prev_position=((4, 7), (5, 7)), expected_position=((5, 7), (6, 7))),
        UpdateCase(event=MoveRightEvent, prev_position=((5, 5), (5, 4)), expected_position=((6, 5), (6, 4))),
        UpdateCase(event=MoveRightEvent, prev_position=((11, 2), (11, 1)), expected_position=((11, 2), (11, 1))),
        UpdateCase(event=MoveRightEvent, prev_position=((11, 0), (11, 1)), expected_position=((11, 0), (11, 1))),
        UpdateCase(event=MoveRightEvent, prev_position=((11, 1), (11, 0)), expected_position=((11, 1), (11, 0))),

        UpdateCase(event=MoveDownEvent, prev_position=((4, 7), (5, 7)), expected_position=((4, 6), (5, 6))),
        UpdateCase(event=MoveDownEvent, prev_position=((5, 5), (5, 4)), expected_position=((5, 4), (5, 3))),
        UpdateCase(event=MoveDownEvent, prev_position=((2, 0), (1, 0)), expected_position=((2, 0), (1, 0))),
        UpdateCase(event=MoveDownEvent, prev_position=((2, 0), (2, 1)), expected_position=((2, 0), (2, 1))),
        UpdateCase(event=MoveDownEvent, prev_position=((2, 1), (2, 0)), expected_position=((2, 1), (2, 0))),
    )

    for case in cases:
        event = case.event
        prev_position = case.prev_position
        expected_position = case.expected_position

        logic = Logic()
        logic.update()

        puyo_A, puyo_B = Puyo(logic), Puyo(logic)
        puyo_A.position, puyo_B.position = prev_position

        current_puyo = CurrentPuyo(puyo_A, puyo_B)

        current_puyo.moving_update(event())
        assert (current_puyo.main_puyo.position, current_puyo.sub_puyo.position) == expected_position


def test_spinning_update():
    '''
    z/x 양방향 회전이 잘 적용되는지 테스트
    '''
    cases = (
        UpdateCase(event=LeftSpinEvent, prev_position=((4, 7), (5, 7)), expected_position=((4, 7), (4, 8))),
        UpdateCase(event=LeftSpinEvent, prev_position=((5, 5), (5, 4)), expected_position=((5, 5), (6, 5))),
        UpdateCase(event=LeftSpinEvent, prev_position=((0, 0), (0, 1)), expected_position=((0, 0), (0, 1))),
        UpdateCase(event=LeftSpinEvent, prev_position=((0, 1), (0, 0)), expected_position=((0, 1), (1, 1))),

        UpdateCase(event=RightSpinEvent, prev_position=((4, 7), (5, 7)), expected_position=((4, 7), (4, 6))),
        UpdateCase(event=RightSpinEvent, prev_position=((5, 5), (5, 4)), expected_position=((5, 5), (4, 5))),
        UpdateCase(event=RightSpinEvent, prev_position=((11, 2), (11, 1)), expected_position=((11, 2), (10, 2))),
        UpdateCase(event=RightSpinEvent, prev_position=((11, 0), (11, 1)), expected_position=((11, 0), (11, 1))),
        UpdateCase(event=RightSpinEvent, prev_position=((11, 1), (11, 0)), expected_position=((11, 1), (10, 1))),
    )

    for case in cases:
        event = case.event
        prev_position = case.prev_position
        expected_position = case.expected_position

        logic = Logic()
        logic.update()

        puyo_A, puyo_B = Puyo(logic), Puyo(logic)
        puyo_A.position, puyo_B.position = prev_position

        current_puyo = CurrentPuyo(puyo_A, puyo_B)

        current_puyo.spinning_update(event())
        assert (current_puyo.main_puyo.position, current_puyo.sub_puyo.position) == expected_position
