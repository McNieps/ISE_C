import pygame

from isec.environment.base.scene import Scene, Camera


class TilemapScene(Scene):
    EMPTY_TILE = -1

    def __init__(self,
                 tilemap: list[list[int]],
                 tileset: dict[int, pygame.Surface],
                 surface: pygame.Surface = None) -> None:

        super().__init__(surface)

        self.tilemap = tilemap
        self.tileset = tileset

        if not self._check_tileset_validity():
            raise ValueError("Invalid tileset")

    def _check_tileset_validity(self) -> bool:
        return all(tile in self.tileset for row in self.tilemap for tile in row)

    def render(self,
               camera: Camera = None) -> None:

        if camera is None:
            camera = self.camera

        for y, row in enumerate(self.tilemap):
            for x, tile in enumerate(row):
                if tile != self.EMPTY_TILE:
                    self.surface.blit(self.tileset[tile],
                                      camera.get_offset(pygame.math.Vector2(x * 32, y * 32)))

    def enhanced_render(self,
                        camera: Camera = None) -> None:

        if camera is None:
            camera = self.camera

        start_x = int(camera.position.x / 32)
        start_y = int(camera.position.y / 32)

        for y, row in enumerate(self.tilemap[start_y:]):
            for x, tile in enumerate(row[start_x:]):
                if tile != self.EMPTY_TILE:
                    self.surface.blit(self.tileset[tile],
                                      camera.get_offset(pygame.math.Vector2((x + start_x) * 32, (y + start_y) * 32)))

    def enhanced_render_2(self,
                          camera: Camera = None) -> None:

        if camera is None:
            camera = self.camera

        start_x = int(camera.position.x / 32)
        start_y = int(camera.position.y / 32)

        end_x = start_x + int(self.rect.width / 32)
        end_y = start_y + int(self.rect.height / 32)

        for y, row in enumerate(self.tilemap[start_y:end_y]):
            for x, tile in enumerate(row[start_x:end_x]):
                if tile != self.EMPTY_TILE:
                    self.surface.blit(self.tileset[tile],
                                      camera.get_offset(pygame.math.Vector2((x + start_x) * 32, (y + start_y) * 32)))


tilemap = [[TilemapScene.EMPTY_TILE for _ in range(100)] for _ in range(100)]
# Draw a 32x32 circle at (32, 32) using numpy.
import numpy as np


def draw_circle(tilemap: list[list[int]],
                x: int,
                y: int,
                radius: int,
                tile: int) -> None:
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if np.sqrt((x - i) ** 2 + (y - j) ** 2) <= radius:
                tilemap[j][i] = tile


draw_circle(tilemap, 32, 32, 16, 0)

tileset = {0: pygame.Surface((32, 32), pygame.SRCALPHA)}
pygame.draw.circle(tileset[0], (255, 255, 255), (16, 16), 16)

for row in tilemap:
    print(row)
