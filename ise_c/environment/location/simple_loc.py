import pygame

from collections.abc import Iterable
from ise_c.environment.location.static_loc import StaticLoc


class SimpleLoc(StaticLoc):
    """
    A basic class used to position a sprite inside a space.

    Feature:
        - x  y   position
        - vx vy  speed
        - a      angle
        - va     angular speed
    """

    def __init__(self,
                 position: Iterable = None,
                 speed: Iterable = None,
                 a: float = 0,
                 va: float = 0,
                 **kwargs):

        super().__init__(position, **kwargs)

        if speed is not None:
            self.speed = pygame.math.Vector2(*speed)
        else:
            self.speed = pygame.math.Vector2(0, 0)

        self.a = a
        self.va = va

    @property
    def vx(self):
        return self.speed[0]

    @property
    def vy(self):
        return self.speed[1]


if __name__ == '__main__':
    x = StaticLoc(position=(0, 5))
    print(x.x)
    print(x.y)
