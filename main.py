import asyncio

from ise.app.app import App
from ise.instance.splash_screen import Splash


async def main():
    App.init("assets/")
    x = Splash()
    await x.run()


asyncio.run(main())
