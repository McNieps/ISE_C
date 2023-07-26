import asyncio

from ise.instance.handlers import LoopHandler, EventHandler


class BaseInstance:
    def __init__(self):
        self.event_handler = EventHandler()
        self.event_handler.register_quit_callback(LoopHandler.stop_game)
        self.fps = 60

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
