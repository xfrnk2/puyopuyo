from timer import Timer
from renderer import Renderer

Timer.init()
a = Renderer()

while True:
    Timer.capture_time()

    a.render()