from ise.instance.handlers.loop_handler import LoopHandler


class InstanceHandler:
    def __init__(self):
        return

    def launch(self):
        LoopHandler.launch_instance(self)

    async def run(self):
        pass