from showobject import Showobject, Timer

class Blink(Showobject):

    def __init__(self, on_time: int, off_time: int, start_value=False) -> None:
        super().__init__()
        self._on_time = on_time
        self._off_time = off_time
        self._time_passed: int = 0

        self.value = start_value

    def update(self, timer: Timer):
        super().update(timer)
        self._time_passed += timer.dt_ms

        #output is on -> turn off
        if self.value and self._time_passed > self._on_time:
            self.value = False
            self._time_passed = 0
        
        #output is off -> turn on
        if not self.value and self._time_passed > self._off_time:
            self.value = True
            self._time_passed = 0            

        