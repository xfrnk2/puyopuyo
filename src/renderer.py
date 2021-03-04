from src.timer import Timer
import os

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        os.system('clear')


class Renderer:

    def __init__(self):
        self.accumulated_elapsed_time = Timer.get_elapsed()
        self.prev_tick = 0.0
        self.fps = 0
        self.fps_count = 0
        self.field = None

    def renderable(self) -> bool:
        elapsed_time = Timer.get_elapsed()
        self.accumulated_elapsed_time += elapsed_time
        self.prev_tick += elapsed_time

        if self.accumulated_elapsed_time < 0.2:
            return False

        self.accumulated_elapsed_time = 0.0
        self.fps_count += 1

        if self.prev_tick > 1.0:
            self.fps, self.fps_count = self.fps_count, 0
            self.prev_tick -= 1.0

        clear()
        return True

