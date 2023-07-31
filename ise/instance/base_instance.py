import asyncio

from ise.app.resource import Resource
from ise.instance.handlers import LoopHandler, EventHandler


class BaseInstance:
    def __init__(self,
                 fps: int = None):

        if fps is None:
            fps = Resource.data["instances"]["default"]["fps"]

        self.event_handler = EventHandler()
        self.event_handler.register_quit_callback(LoopHandler.stop_game)
        self.fps = fps

    async def setup(self):
        return

    async def loop(self):
        return

    async def finish(self):
        return

    async def execute(self):
        await self.setup()
        LoopHandler.stack.append(self)

        while LoopHandler.is_running(self):
            LoopHandler.limit_and_get_delta(self.fps)
            await self.loop()
            await asyncio.sleep(0)

        await self.finish()
