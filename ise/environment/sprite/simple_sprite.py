import pygame
import typing

from collections.abc import Iterable

from ise.objects.cached_surface import CachedSurface
from ise.environment.sprite.rendering_techniques import RenderingTechniques


class SimpleSprite:
    __slots__ = ["surface", "rect", "effective_rect", "effective_surface", "rendering_technique"]

    def __init__(self,
                 surface: pygame.Surface) -> None:
        """Initialize sprite."""

        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.center = 0, 0

        self.effective_surface = self.surface.copy()
        self.effective_rect = self.rect.copy()

        self.rendering_technique = RenderingTechniques.static

    def update(self,
               delta: float) -> None:
        """Update sprite."""

        pass

    def set_rendering_technique(self,
                                rendering_technique: typing.Literal["static", "rotated", "cached"]) -> None:
        """Set rendering technique."""

        if rendering_technique == "static":
            self.rendering_technique = RenderingTechniques.static

        elif rendering_technique == "rotated":
            self.rendering_technique = RenderingTechniques.rotated

        elif rendering_technique == "cached":
            if not isinstance(self.surface, CachedSurface):
                raise ValueError("Cached rendering technique requires cached surface.")
            self.rendering_technique = RenderingTechniques.cached

        else:
            raise ValueError("Invalid rendering technique.")

    def render(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: Iterable,
               angle: float) -> None:
        """Render sprite."""

        self.rendering_technique(self,
                                 destination,
                                 destination_rect,
                                 offset,
                                 angle)
