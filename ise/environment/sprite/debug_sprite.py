import pygame

from ise.environment.sprite.simple_sprite import SimpleSprite


class DebugSprite(SimpleSprite):
    def __init__(self,
                 radius: int = 9) -> None:

        surface = pygame.Surface((radius*2+1, radius*2+1))
        surface.set_colorkey((0, 0, 0))

        pygame.draw.line(surface, (255, 0, 0), (radius, radius), (radius*2+1, radius), 1)
        pygame.draw.line(surface, (0, 255, 0), (radius, radius), (radius, 0), 1)
        pygame.draw.ellipse(surface, (0, 0, 255), pygame.Rect(radius-1, radius-1, 3, 3))

        super().__init__(surface)


if __name__ == '__main__':
    x = DebugSprite()
