import pygame

from collections.abc import Iterable

from isec.environment.position import StaticPos
from isec.environment.sprite import SimpleSprite


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
               surface: pygame.Surface,
               rect: pygame.Rect) -> None:
        """Render elements of this container."""

        self.sprite.render(surface, rect, camera_offset, self.position.a)
