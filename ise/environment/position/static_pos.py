import pygame

from collections.abc import Iterable


class StaticPos:
    """
    A very simple class used to position a sprite inside a space.

    Feature:
        - x y  position.
    """

    def __init__(self,
                 position: Iterable = None,
                 **kwargs):

        if position is not None:
            self.position = pygame.math.Vector2(*position)
        else:
            self.position = pygame.math.Vector2(0, 0)

    def update(self,
               delta: float) -> None:
        """
        Update position.

        Nothing will happen because this position is static.
        """
        return

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]


if __name__ == '__main__':
    x = StaticPos(position=(0, 5))
    print(x.x)
    print(x.y)