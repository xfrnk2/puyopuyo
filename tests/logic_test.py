import sys
sys.path.append('C:/Users/rad87/Documents/programming/puyopuyo')

from dataclasses import dataclass
from src.logic import Logic

@dataclass
class ValidCoordinatesCase:
    position: tuple
    expected: bool

def test_valid_coordinates():
    cases=(ValidCoordinatesCase(position=(12,20), expected=False),
           ValidCoordinatesCase(position=(-1,6), expected=False),
           ValidCoordinatesCase(position=(0, 3), expected=True),
           ValidCoordinatesCase(position=(11, 19), expected=True)
           )
    logic = Logic()

    for case in cases:
        assert logic.valid_coordinates(case.position) == case.expected
