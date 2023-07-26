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
        pygame.draw.ellipse(surface_2, (0, 0, 255), pygame.Rect(radius - 2, radius - 2, 5, 5))
        pygame.draw.ellipse(surface_2, (255, 255, 255), pygame.Rect(radius - 1, radius - 1, 3, 3))

        surface_3 = surface_1.copy()
        pygame.draw.ellipse(surface_3, (255, 255, 255), pygame.Rect(radius - 2, radius - 2, 5, 5))
        pygame.draw.ellipse(surface_3, (0, 0, 255), pygame.Rect(radius - 1, radius - 1, 3, 3))

        super().__init__(surfaces=[surface_1, surface_2, surface_3], frame_durations=[1.0, 0.1, 0.1], loop=True)


if __name__ == '__main__':
    x = DebugSprite()
