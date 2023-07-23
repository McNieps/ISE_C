import pygame

from ise.environment.sprite.animated_sprite import AnimatedSprite


class DebugSprite(AnimatedSprite):
    def __init__(self,
                 radius: int = 9) -> None:

        surface_1 = pygame.Surface((radius * 2 + 1, radius * 2 + 1))
        surface_1.set_colorkey((0, 0, 0))

        pygame.draw.line(surface_1, (255, 0, 0), (radius, radius), (radius * 2 + 1, radius), 1)
        pygame.draw.line(surface_1, (0, 255, 0), (radius, radius), (radius, 0), 1)
        pygame.draw.ellipse(surface_1, (0, 0, 255), pygame.Rect(radius - 1, radius - 1, 3, 3))

        surface_2 = surface_1.copy()
        surface_2 = pygame.transform.rotate(surface_2, 90)

        super().__init__(surfaces=[surface_1, surface_2], frame_durations=[1.0, 1.0], loop=True)


if __name__ == '__main__':
    x = DebugSprite()
