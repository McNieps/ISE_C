import pygame

from ise.environment.entity import Entity
from ise.environment.sprite import DebugSprite
from ise.environment.position import AdvancedPos


class RotatingEntity(Entity):
    def __init__(self) -> None:
        position = AdvancedPos(position=(200, 200), speed=(1, 0), va=10)

        super().__init__(position, DebugSprite())

    def update(self,
               delta: float) -> None:
        super().update(delta)
        # self.position.position.rotate_ip(-self.position.va*delta)
        self.position.speed = pygame.Vector2(self.position.speed.magnitude(), 0).rotate(-self.position.a)
        print(self.position.a)
