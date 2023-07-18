import pygame

from collections.abc import Iterable


class SimpleSprite:
    __slots__ = ["surface", "rect", "effective_rect"]

    def __init__(self,
                 surface: pygame.Surface) -> None:

        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.center = 0, 0

        self.effective_rect = self.rect.copy()

    def update(self,
               delta: float) -> None:
        pass

    def render(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: Iterable,
               _angle: float) -> None:

        self.effective_rect = self.rect.move(*offset)

        if not self.effective_rect.colliderect(destination_rect):
            return

        destination.blit(self.surface, self.effective_rect)
