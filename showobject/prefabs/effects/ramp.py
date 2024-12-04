from showobject import Showobject
from showobject.timer import Timer

class Ramp(Showobject):


    def __init__(self, initial_value:float = 0.0) -> None:
        self.value = initial_value
        self._time_passed = 0
        self._duration = 0
        self._target_value = 0

    def update(self, timer: Timer):
        self._time_passed += timer.dt_ms
        t = self._time_passed / self._duration
        if t <= 1:
            self.value = t * self._target_value
        else:
            self.value = self._target_value
    
    
    def go(self, value:float, duration_ms: int):
        self._duration = duration_ms
        self._time_passed = 0
        self._target_value = value
