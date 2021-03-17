import os

FREQUENCY_PER_SECOND = 5

# Windows
if os.name == 'nt':
    def clear():
        os.system('cls')

# Posix (Linux, OS X)
else:
    def clear():
        os.system('clear')


class Renderer:

    def __init__(self, frequency=FREQUENCY_PER_SECOND):
        self.__frequency = frequency
        self.__elapsed_time = 0.0
        self.__fps = 0
        self.__fps_count = 0
        self.__field = None

    @property
    def elapsed_time(self):
        return self.__elapsed_time

    def renderable(self):
        return not self.__elapsed_time < 1.0 / self.__frequency

    def update(self, time):
        self.__elapsed_time += time
        if not self.renderable():
            return
        self.__fps_count += 1
        self.__elapsed_time = 0.0


    def set_field(self, field):
        self.__field = field

    def render(self):

        print(self.__field)
        print(f"FPS : {self.__fps}")
        clear()

        if self.__frequency <= self.__fps_count:
            self.__fps, self.__fps_count = self.__fps_count, 0
