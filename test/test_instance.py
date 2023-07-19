import pygame

from ise.instance.splash_screen import Splash
from ise.instance import LoopHandler, BaseInstance
from ise.environment.scene import Scene
from moving_entity import MovingEntity
from origin_entity import OriginEntity
from rotating_entity import RotatingEntity


class TestInstance(BaseInstance):
    def __init__(self):
        super().__init__()
        self.fps = 60
        self.window = pygame.display.get_surface()

        self.scene = Scene(self.window)
        self.scene.add_entities(MovingEntity(), OriginEntity(), RotatingEntity())

    async def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LoopHandler.stop_instance(self)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    LoopHandler.stop_instance(self)
                if event.key == pygame.K_RETURN:
                    await Splash().execute()

        if pygame.mouse.get_pressed(3)[0]:
            self.scene.camera.position.position -= pygame.math.Vector2(*pygame.mouse.get_rel())/3
            print(f"Camera "
                  f"X: {round(self.scene.camera.position.position[0])}  "
                  f"Y: {round(self.scene.camera.position.position[1])}")
        else:
            pygame.mouse.get_rel()

        for entity in self.scene.entities:
            entity.update(LoopHandler.delta)

        self.window.fill((127, 127, 127))
        self.scene.render()

        pygame.display.flip()
