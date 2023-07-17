import asyncio

from ise.instance.handlers.loop_handler import LoopHandler


class BaseInstance:
    def __init__(self):
        self.fps = 60
        self.delta = 0

    async def setup(self):
        return

    async def loop(self):
        print("EMPTY LOOP. BASEINSTANCE LOOP METHOD MUST BE OVERRIDDEN.")

    async def run(self):
        await self.setup()
        LoopHandler.stack.append(self)

        while LoopHandler.is_running(self):
            LoopHandler.limit_and_get_delta(self.fps)
            await self.loop()
            await asyncio.sleep(0)
