import pygame
import time
import math

from ise.instance.handlers import LoopHandler
from ise.instance.base_instance import BaseInstance


class Splash(BaseInstance):
    def __init__(self):
        super().__init__()
        self.window = pygame.display.get_surface()
        self.launch()

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LoopHandler.stop_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("QUITTING GAME")
                    LoopHandler.stop_game()
                else:
                    print(event.key)

        rect = pygame.Rect(0, 0, 40, 40)
        rect.center = (200+50*math.cos(time.time()), 150)
        self.window.fill((0, 0, 0))
        pygame.draw.rect(self.window, (255, 255, 255), rect)

        pygame.display.flip()


if __name__ == '__main__':
    from ise.app.app import App

    App.init("", default_only=True)
    Splash()
