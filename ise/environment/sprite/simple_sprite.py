import pygame

from collections.abc import Iterable


class SimpleSprite:
    __slots__ = ["surface", "rect", "effective_rect", "effective_surface", "rendering_technique"]

    def __init__(self,
                 surface: pygame.Surface) -> None:

        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.center = 0, 0

        self.effective_surface = self.surface.copy()
        self.effective_rect = self.rect.copy()
        self.rendering_technique = self.render_rotate

    def update(self,
               delta: float) -> None:
        pass

    def toggle_angle(self,
                     enable: bool = None):

        if enable is None:
            if self.rendering_technique is self.render_static:
                self.rendering_technique = self.render_rotate
            else:
                self.rendering_technique = self.render_static
            return

        if enable:
            self.rendering_technique = self.render_rotate
        else:
            self.rendering_technique = self.render_static


    def render(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: Iterable,
               angle: float) -> None:

        self.rendering_technique(destination,
                                 destination_rect,
                                 offset,
                                 angle)

    def render_static(self,
                      destination: pygame.Surface,
                      destination_rect: pygame.Rect,
                      offset: Iterable,
                      _angle: float) -> None:

        self.effective_rect = self.rect.move(*offset)

        if not self.effective_rect.colliderect(destination_rect):
            return

        destination.blit(self.surface, self.effective_rect)

    def render_rotate(self,
                      destination: pygame.Surface,
                      destination_rect: pygame.Rect,
                      offset: Iterable,
                      angle: float) -> None:

        self.effective_surface = pygame.transform.rotate(self.surface, angle)
        self.effective_rect = self.effective_surface.get_rect()
        self.effective_rect.center = self.rect.center

        if not self.effective_rect.colliderect(destination_rect):
            return

        self.effective_rect.move_ip(*offset)
        destination.blit(self.effective_surface, self.effective_rect)
