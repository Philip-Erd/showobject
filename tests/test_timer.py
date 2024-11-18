import context
from showobject import Timer;

import unittest


class BasicTestSuite(unittest.TestCase):
    """Test timer"""

    def test_reset(self):
        timer = Timer()
        timer.tick(50)

        assert timer.ticks_ms != 0
        timer.reset()
        assert timer.ticks_ms == 0

    def test_increment_timer(self):
        timer = Timer()
        timer.tick(16)

        assert timer.ticks_ms == 16
        assert timer.time > 0

    def test_delta_time(self):
        timer = Timer()
        timer.tick(50)
        assert timer.dt_ms == 50
        timer.tick(25)
        assert timer.dt_ms == 25

if __name__ == '__main__':
    unittest.main()