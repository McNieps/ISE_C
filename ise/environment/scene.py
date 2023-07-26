import pygame

from ise.environment.entity import Entity
from ise.environment.camera import Camera


class Scene:
    def __init__(self,
                 surface: pygame.Surface = None):

        self.entities: list[Entity] = []

        if surface is None:
            surface = pygame.display.get_surface()
        self.surface = surface
        self.rect = self.surface.get_rect()

        self.camera = Camera()

    def add_entities(self,
                     *entities) -> None:

        self.entities.extend([entity for entity in entities
                              if entity not in self.entities])

    def update(self,
               delta: float) -> None:

        for entity in self.entities:
            entity.update(delta)

    def render(self,
               camera: Camera = None) -> None:

        if camera is None:
            camera = self.camera

        for entity in self.entities:
            entity.render(camera.get_offset(entity.position), self.surface, self.rect)
