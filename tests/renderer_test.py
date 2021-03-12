from dataclasses import dataclass

from src.renderer import Renderer

FREQUENCY_PER_SECOND = 5


@dataclass
class RendererTestCase:
    time: float
    expected: bool


def test_renderer():
    '''
    경과시간을 제대로 반영하는지 테스트
    '''
    cases = (
        RendererTestCase(time=5.0, expected=False),
        RendererTestCase(time=0.05, expected=True),
        RendererTestCase(time=0.1, expected=True),
        RendererTestCase(time=0.2, expected=False)
    )
    renderer = Renderer(FREQUENCY_PER_SECOND)
    for case in cases:
        prev_elapsed_time = renderer.elapsed_time
        time, expected = case.time, case.expected

        renderer.update(time)
        assert (prev_elapsed_time < renderer.elapsed_time) == expected
