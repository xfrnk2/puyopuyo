from src.renderer import Renderer
from dataclasses import dataclass
from pytest import fixture

@fixture
def Case1():
    mock = Renderer()
    mock.fps_count = 4
    mock.accumulated_elapsed_time = 0.5
    mock.prev_tick = 1.1
    return mock

@fixture
def Case2():
    mock = Renderer()
    mock.accumulated_elapsed_time = 0.1
    return mock

@fixture
def Case3():
    mock = Renderer()
    mock.fps_count = 1
    mock.accumulated_elapsed_time = 0.3
    return mock


def test_renderable1(Case1):
    expected = Case1.renderable()
    assert expected == True
    assert Case1.fps_count == 0 and Case1.fps == 5
    assert Case1.prev_tick <= 1.0

def test_renderable2(Case2):
    expected = Case2.renderable()
    assert expected == False

def test_renderable3(Case3):
    expected =Case3.renderable()
    assert expected == True
    assert Case3.fps_count == 2
