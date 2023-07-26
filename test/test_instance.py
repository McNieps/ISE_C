import pygame

from ise.instance.splash_screen import Splash
from ise.instance import LoopHandler, BaseInstance
from ise.environment.scene import Scene

from moving_entity import MovingEntity
from origin_entity import OriginEntity
from rotating_entity import RotatingEntity
from cached_surf_entity import CachedSurfEntity


class TestInstance(BaseInstance):
    def __init__(self):
        super().__init__()
        self.fps = 120
        self.window = pygame.display.get_surface()

        self.scene = Scene(self.window)
        origin_entity = RotatingEntity()
        self.scene.add_entities(origin_entity)

        self.gui = Scene(self.window)
        self.gui.add_entities(origin_entity)

        def move_camera() -> None:
            self.scene.camera.position.position -= pygame.math.Vector2(self.event_handler.mouse_rel)/3

        self.event_handler.register_buttonpressed_callback(0, move_camera)

    async def loop(self):
        self.event_handler.handle_events()

        self.scene.update(LoopHandler.delta)
        self.gui.update(LoopHandler.delta)

        self.window.fill((127, 127, 127))
        self.scene.render()
        self.gui.render()

        pygame.display.flip()


if __name__ == '__main__':
    import asyncio

    from ise.app.app import App


    async def main():
        App.init("../assets/")
        x = TestInstance()
        await x.execute()


    asyncio.run(main())
