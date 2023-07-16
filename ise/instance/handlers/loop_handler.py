import pygame
import asyncio
import sys


class LoopHandler:
    stack: list[str] = []

    _clock: pygame.time.Clock = pygame.time.Clock()
    _run: bool = True
    _delta: float = 0

    @classmethod
    def launch_instance(cls,
                        instance) -> None:

        cls.stack.append(instance.__class__.__name__)
        asyncio.run(instance.run())
        cls.stack.pop(-1)

    @classmethod
    def is_running(cls):
        if cls._run is False:
            cls._run = True
            return False

        return True

    @classmethod
    def limit_and_get_delta(cls,
                            fps: int):

        cls._delta = cls._clock.tick(fps)/1000
        return cls._delta

    @classmethod
    def stop_instance(cls) -> None:
        cls._run = False

    @classmethod
    def stop_game(cls):
        sys.exit()
