import pygame

from collections.abc import Iterable

from ise.environment.position import StaticPos


class Camera:
    def __init__(self,
                 position: Iterable = None) -> None:

        if position is None:
            self.position = StaticPos()
        else:
            self.position = StaticPos(*position)

    def get_offset(self,
                   position: StaticPos) -> pygame.math.Vector2:

        return position.position - self.position.position
