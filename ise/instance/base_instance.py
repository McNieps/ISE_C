import asyncio

from ise.instance.handlers.loop_handler import LoopHandler


class BaseInstance:
    def __init__(self):
        self.fps = 60
        self.delta = 0

    def launch(self):
        LoopHandler.launch_instance(self)

    def loop(self):
        print("EMPTY LOOP. BASEINSTANCE LOOP METHOD MUST BE OVERRIDED.")

    async def run(self):
        while LoopHandler.is_running():
            self.delta = LoopHandler.limit_and_get_delta(self.fps)
            self.loop()
            await asyncio.sleep(0)
