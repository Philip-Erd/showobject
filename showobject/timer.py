

class Timer:
    '''
        simple Timer to keep track of delta time and time since last reset

        Attributes:
        ticks_ms: int 
            elapsed time since last reset in milliseconds
        time: float
            elapsed time since last reset in seconds
        dt_ms: int
            delta time in milliseconds
        dt: float
            delta time in seconds
    '''
    def __init__(self):
        self.reset()

    def reset(self):
        '''resets all values back to zero'''
        self.ticks_ms: int = 0
        self.time: float = 0.0
        self.dt_ms: int = 0
        self.dt: float = 0

    def __str__(self):
        return F"ticks_ms: {self.ticks_ms}\ntime: {self.time}\ndt_ms: {self.dt_ms}\ndt: {self.dt}"

    def tick(self, dt_ms: int):
        '''advances the Timer by the given amount of milliseconds'''
        self.dt_ms = dt_ms
        self.dt = dt_ms / 1000.0
        self.ticks_ms += dt_ms
        self.time = self.ticks_ms / 1000.0
        pass 