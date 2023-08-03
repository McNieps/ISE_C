import pygame
import numpy
import time

from isec.app import Resource
from isec.instance import LoopHandler, BaseInstance
from isec.environment.scene import TilemapScene, EntityScene
from isec.environment.sprite import SimpleSprite
from isec.environment.position import SimplePos
from isec.environment.base.entity import Entity


def draw_circle(_tilemap: list[list[int]],
                x: int,
                y: int,
                radius: int,
                tile: int) -> None:
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if numpy.sqrt((x - i) ** 2 + (y - j) ** 2) <= radius:
                _tilemap[j][i] = tile


tile_map = [[0 for _ in range(400)] for _ in range(38)]
tile_set = {-1: None, 0: pygame.Surface((8, 8))}
pygame.draw.circle(tile_set[0], (255, 255, 255), (4, 4), 4)


class TestInstance(BaseInstance):
    def __init__(self):
        super().__init__(fps=1200)

        self.scene = TilemapScene(Resource.data["maps"]["stock"], tile_set)
        self.top_scene = EntityScene()
        self.test_entity = Entity(SimplePos(), SimpleSprite(Resource.image["stock"]["face"],
                                                            blit_flag=pygame.BLEND_SUB))
        self.top_scene.add_entities(self.test_entity)

        self.event_handler.register_buttonpressed_callback(2, self.move_camera)
        self.event_handler.register_buttondown_callback(4, self.increment_inter_tile)
        self.event_handler.register_buttonup_callback(5, self.decrement_inter_tile)

    async def loop(self):
        self.scene.update(LoopHandler.delta)
        LoopHandler.fps_caption()
        self.window.fill((127, 127, 127))

        self.scene.render()
        self.top_scene.render()

    # region Callback
    def move_camera(self) -> None:
        self.scene.camera.position.position -= pygame.math.Vector2(self.event_handler.mouse_rel)/3
        self.top_scene.camera.position.position -= 2*pygame.math.Vector2(self.event_handler.mouse_rel)/3

    def increment_inter_tile(self):
        self.scene.inter_tile_distance += 1

    def decrement_inter_tile(self):
        self.scene.inter_tile_distance -= 1

    # endregion


if __name__ == '__main__':
    import asyncio

    from isec.app.app import App


    async def main():
        App.init("../isec/assets/")
        x = TestInstance()
        await x.execute()

    asyncio.run(main())
