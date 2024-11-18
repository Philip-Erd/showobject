import showobject
from showobject import Timer, Showobject
from showobject.prefabs import Blink

import asyncio
import time


class RootObject(Showobject):
    
    def __init__(self) -> None:
        super().__init__()
        # add other Showobjects or more variables
        self.blink = Blink(1000, 500)

        self.value: float = 0.0

    def update(self, timer: Timer):
        #update other Showobjects
        self.blink.update(timer)

        print(self.blink.value)

        self.value += timer.dt
        if self.value > 1.0:
            print("value is > 1")
            self.value = 0.0


async def main():
    root = RootObject()
    timer = Timer()

    last_update= round(time.time() * 1000)

    while(True):
        #tick timer
        current_time = round(time.time() * 1000)
        delta_time = current_time - last_update
        last_update = current_time

        timer.tick(delta_time)


        #update root
        root.update(timer)

        #wait a bit
        await asyncio.sleep(0.2)


if __name__ == "__main__":
    asyncio.run(main())




