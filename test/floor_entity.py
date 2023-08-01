import pygame

from isec.environment import Entity
from isec.environment.position import PymunkPos
from isec.environment.sprite import AnimatedSprite
from isec.environment.sprite.pymunk_sprite import PymunkSprite
from isec.app.resource import Resource


class FloorEntity(Entity):
    def __init__(self,
                 rect: pygame.Rect = pygame.Rect(0, 280, 400, 20)) -> None:

        self.rect = rect
        position = PymunkPos(position=rect.center, base_shape_friction=5, body_type=PymunkPos.TYPE_STATIC)
        real_surface = pygame.Surface(rect.size)
        real_surface.fill((255, 50, 100))
        pygame.draw.rect(real_surface, (0, 0, 0), (0, 0, *rect.size), 5)  # Draw the outline of the rectangle
        position.create_rect_shape(real_surface, radius=0)

        pymunk_surface = PymunkSprite(position, "static").surface

        self.body = position.body
        self.shapes = position.shapes

        sprite = AnimatedSprite([real_surface, pymunk_surface],
                                rendering_technique="static",
                                frame_durations=[1, 1])

        sprite.set_rendering_technique("static")

        super().__init__(position, sprite)

