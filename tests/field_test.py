from dataclasses import dataclass

from pytest import fixture

from src.field import LogicField
from src.game_object import GameObject


@fixture()
def game_object():
    mock = GameObject()
    return mock

class AlreadyExistCase:
    position: tuple
    game_object: GameObject
    expected: bool

def test_already_exist():
    cases = (AlreadyExistCase(
        posotion=(1, 1),
        game_object=game_object,
        expected=True
    ))
    logic_field = LogicField()
    for case in cases:
        x, y = case.position
        #assert 0 <= 20 - case.position[1]  - 1 < 20
        target = logic_field[logic_field.height - y  - 1][x]
        target and garget != case.game_object
