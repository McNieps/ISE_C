import asyncio

from isec.app.app import App
from isec.instance.splash_screen import Splash


async def main():
    App.init("isec/assets/")
    x = Splash()
    await x.execute()


asyncio.run(main())
