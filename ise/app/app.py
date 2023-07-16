import pygame

from ise.app.resource import Resource
from ise.ise_typing import PathLike


class App:
    window: pygame.Surface = None

    @classmethod
    def init(cls,
             assets_dir: PathLike,
             default_safeguard: bool = True,
             default_only: bool = False) -> None:

        Resource.set_directory(assets_dir)
        Resource.pre_init(default_safeguard, default_only)
        App.create_window()
        Resource.init(default_safeguard, default_only)

    @classmethod
    def create_window(cls):
        window_size = Resource.data["window"]["size"]
        window_flag = Resource.data["window"]["scaled"] * 512
        window_flag |= Resource.data["window"]["fullscreen"] * -2147483648
        cls.window = pygame.display.set_mode(window_size, window_flag)
