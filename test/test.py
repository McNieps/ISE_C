import asyncio

from ise.app.app import App
from test_instance import TestInstance


async def main():
    App.init("../assets/")
    x = TestInstance()
    await x.execute()


asyncio.run(main())
