import pygame

from collections.abc import Iterable

from ise.environment.position import StaticPos
from ise.environment.sprite import SimpleSprite


class Entity:
    def __init__(self,
                 position: StaticPos,
                 sprite: SimpleSprite) -> None:

        self.position: StaticPos = position
        self.sprite: SimpleSprite = sprite

    def update(self,
               delta: float) -> None:
        """Update elements of this container."""

        self.position.update(delta)
        self.sprite.update(delta)

    def render(self,
               camera_offset: Iterable,
               camera_angle: float,
               surface: pygame.Surface,
               rect: pygame.Rect) -> None:
        """Render elements of this container."""

        effective_angle = camera_angle + self.position.a
        self.sprite.render(surface, rect, camera_offset, effective_angle)
