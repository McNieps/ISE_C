import pygame

from collections.abc import Iterable


class RenderingTechniques:
    @staticmethod
    def static(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: Iterable,
               _angle: float) -> None:

        self.effective_surf = self.surface
        self.effective_rect = self.rect.move(*offset)

        if not self.effective_rect.colliderect(destination_rect):
            return

        destination.blit(self.surface, self.effective_rect)

    @staticmethod
    def rotated(self,
                destination: pygame.Surface,
                destination_rect: pygame.Rect,
                offset: Iterable,
                angle: float) -> None:

        self.effective_surface = pygame.transform.rotate(self.surface, angle)
        self.effective_rect = self.effective_surface.get_rect()
        self.effective_rect.center = self.rect.move(*offset).center

        if not self.effective_rect.colliderect(destination_rect):
            return

        destination.blit(self.effective_surface, self.effective_rect)

    @staticmethod
    def cached(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: Iterable,
               angle: float) -> None:

        self.effective_surface = self.surface[angle]
        self.effective_rect = self.effective_surface.get_rect()
        self.effective_rect.center = self.rect.move(*offset).center

        if not self.effective_rect.colliderect(destination_rect):
            return

        destination.blit(self.effective_surface, self.effective_rect)