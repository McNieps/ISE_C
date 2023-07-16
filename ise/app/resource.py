import pygame

from ise.ise_typing import PathLike


class Resource:
    _default_assets_directory: PathLike = None
    _project_assets_directory: PathLike = None

    data: dict[str: dict[str: any]]
    image: dict[str: dict[str: any]]
    sound: dict[str: dict[str: any]]

    @classmethod
    def set_directory(cls,
                      assets_dir: PathLike) -> None:

        cls._project_assets_directory = assets_dir

    @classmethod
    def pre_init(cls,
                 default_safeguard: bool = True,
                 default_only: bool = False) -> None:

        if default_safeguard or default_only:
            cls._get_default_assets_directory()
            cls._load_data(cls._default_assets_directory)

        if not default_only:
            cls._load_data(cls._project_assets_directory)

    @classmethod
    def init(cls,
             default_safeguard: bool = True,
             default_only: bool = False) -> None:

        if default_safeguard or default_only:
            cls._get_default_assets_directory()
            cls._load_image(cls._default_assets_directory)
            cls._load_sound(cls._default_assets_directory)

        if not default_only:
            cls._load_image(cls._project_assets_directory)
            cls._load_sound(cls._project_assets_directory)

    @classmethod
    def _get_default_assets_directory(cls):
        if cls._default_assets_directory is not None:
            return

        list_path = str(__file__).split("\\")
        cls.assets_directory = "/".join(list_path[:list_path.index("ISE-C")+1]) + "/"

    @classmethod
    def _load_data(cls,
                   assets_path: PathLike) -> None:
        pass

    @classmethod
    def _load_image(cls,
                    assets_path: PathLike) -> None:
        pass

    @classmethod
    def _load_sound(cls,
                    assets_path: PathLike) -> None:
        pass
