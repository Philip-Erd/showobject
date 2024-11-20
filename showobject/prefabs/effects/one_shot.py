from showobject import Showobject, Timer


class OneShot(Showobject):
    """
    Turns value on for the given amount of time.

    Attributes:
    value: bool
        is True when firing is on and False otherwise
    """

    def __init__(self) -> None:
        self._time_passed: int = 0
        self._duration: int = 0

        self.value = False

    def fire(self, duration: int):
        '''Turns value on for given duration in ms'''
        self._duration = duration
        self._time_passed = 0


    def update(self, timer: Timer):
        self._time_passed += timer.dt_ms
        self.value = True if self._time_passed < self._duration else False
