from showobject import Showobject, Timer

class Blink(Showobject):
    '''
        Turn value on and off depending on the given on and off time.

        Attributes:
        value: bool
            is True when blink is on and False otherwise
    '''

    def __init__(self, on_time: int, off_time: int) -> None:
        self._on_time = on_time
        self._total_time = on_time + off_time

        self.value = False

    def update(self, timer: Timer):
         self.value = False if timer.ticks_ms % self._total_time > self._on_time else True
        