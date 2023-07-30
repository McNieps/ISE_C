import pygame

from ise.app import Resource
from ise.instance import LoopHandler, BaseInstance
from ise.environment.scene import Scene

from rotating_entity import RotatingEntity
from physic_entity import PhysicEntity
from floor_entity import FloorEntity


class TestInstance(BaseInstance):
    def __init__(self):
        super().__init__()
        self.fps = 120
        self.window = pygame.display.get_surface()

        origin_entity = RotatingEntity()
        self.physic_entity = PhysicEntity()
        origin_entity.position = self.physic_entity.position

        self.scene = Scene(self.window)
        self.scene.space.gravity = (0, 500)

        self.scene.add_entities(self.physic_entity)
        self.scene.add_entities(origin_entity)

        def spawn_entity() -> None:
            print("Spawning!")
            spawn_point = pygame.math.Vector2(pygame.mouse.get_pos()) + self.scene.camera.position.position
            physic_entity = PhysicEntity(position=spawn_point)
            debug_entity = RotatingEntity()
            debug_entity.position = physic_entity.position
            self.scene.add_entities(physic_entity, debug_entity)

        def clean_entities() -> None:
            self.scene.space.remove(*self.scene.space.bodies, *self.scene.space.shapes)

        self.event_handler.register_keydown_callback(pygame.K_w, self.create_walls)
        self.event_handler.register_keydown_callback(pygame.K_c, clean_entities)
        self.event_handler.register_buttondown_callback(1, spawn_entity)

        def move_camera() -> None:
            self.scene.camera.position.position -= pygame.math.Vector2(self.event_handler.mouse_rel)/3

        self.event_handler.register_buttonpressed_callback(1, move_camera)

    def create_walls(self):
        self.scene.add_entities(FloorEntity())
        self.scene.add_entities(FloorEntity(pygame.Rect(0, 0, 20, 300)))
        self.scene.add_entities(FloorEntity(pygame.Rect(380, 0, 20, 300)))
        self.scene.add_entities(FloorEntity(pygame.Rect(0, 0, 400, 20)))

    async def loop(self):
        self.event_handler.handle_events()

        self.scene.update(LoopHandler.delta)
        self.window.fill((127, 127, 127))
        self.scene.render()

        pygame.display.flip()


if __name__ == '__main__':
    import asyncio

    from ise.app.app import App


    async def main():
        App.init("../assets/")
        x = TestInstance()
        await x.execute()


    asyncio.run(main())
