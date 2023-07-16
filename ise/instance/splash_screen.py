import pygame

from ise.instance.handlers import InstanceHandler, LoopHandler


class Splash(InstanceHandler):
    def __init__(self):
        """
        Used for variables definition
        """

        super().__init__()

        self.launch()

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("QUITTING GAME")
                    LoopHandler.stop_game()




x = Splash()
