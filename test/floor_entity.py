import pygame

from ise.environment import Entity
from ise.environment.position import PymunkPos
from ise.environment.sprite import SimpleSprite
from ise.app.resource import Resource


class FloorEntity(Entity):
    def __init__(self,
                 rect: pygame.Rect = pygame.Rect(0, 280, 400, 20)) -> None:

        self.rect = rect
        position = PymunkPos(position=rect.center, body_type=PymunkPos.TYPE_STATIC)
        surface = pygame.Surface(rect.size)
        surface.fill((255, 50, 100))
        pygame.draw.rect(surface, (0, 0, 0), (0, 0, *rect.size), 5)  # Draw the outline of the rectangle
        sprite = SimpleSprite(surface, rendering_technique="static")
        position.create_rect_shape(surface)

        self.body = position.body
        self.shapes = position.shapes

        sprite.set_rendering_technique("static")

        super().__init__(position, sprite)

