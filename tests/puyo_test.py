import sys
sys.path.append('C:/Users/rad87/Documents/programming/puyopuyo')
from src.puyo import Puyo

def test_location():
    puyo = Puyo()
    assert puyo.get_location() == (1, 1)
