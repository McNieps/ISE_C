import pygame
import json
import os

from ise.ise_typing import PathLike
from ise.ise_error import InvalidFileFormatError


class Resource:
    _default_assets_directory: PathLike = None
    _project_assets_directory: PathLike = None

    data: dict[str: dict[str: any]] = {}
    image: dict[str: dict[str: any]] = {}
    sound: dict[str: dict[str: any]] = {}

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
        cls._default_assets_directory = "/".join(list_path[:list_path.index("ISE-C")+1]) + "/assets/"

    @classmethod
    def _load_data(cls,
                   assets_path: PathLike,
                   current_dict: dict = None) -> None:

        if current_dict is None:
            current_dict = cls.data
            assets_path += "data/"

        for elem in os.scandir(assets_path):
            if elem.is_dir():
                if elem.name not in current_dict:
                    current_dict[elem.name] = {}

                cls._load_data(assets_path+elem.name+"/", current_dict[elem.name])

            if elem.is_file():
                key_name = "".join(elem.name.split(".")[:-1])

                if elem.name.endswith(".json"):
                    if key_name not in current_dict:
                        current_dict[key_name] = {}

                    current_dict[key_name] |= cls._load_json(assets_path+elem.name)

                else:
                    raise InvalidFileFormatError(f"{elem.name.split('.')[-1]} is not a supported data file format")

    @classmethod
    def _load_json(cls,
                   file_path: PathLike) -> dict[str, ...]:

        with open(file_path) as file:
            return json.load(file)

    @classmethod
    def _load_image(cls,
                    assets_path: PathLike,
                    current_dict: dict = None) -> None:

        if current_dict is None:
            current_dict = cls.image
            assets_path += "image/"

        for elem in os.scandir(assets_path):
            if elem.is_dir():
                if elem.name not in current_dict:
                    current_dict[elem.name] = {}

                cls._load_image(assets_path + elem.name + "/", current_dict[elem.name])

            if elem.is_file():
                key_name = "".join(elem.name.split(".")[:-1])

                if any(elem.name.endswith(ext) for ext in [".png", ".jpg"]):
                    current_dict[key_name] = pygame.image.load(assets_path + elem.name).convert_alpha()

                else:
                    raise InvalidFileFormatError(f"{elem.name.split('.')[-1]} is not a supported image file format")

    @classmethod
    def _load_sound(cls,
                    assets_path: PathLike,
                    current_dict: dict = None) -> None:

        if current_dict is None:
            current_dict = cls.sound
            assets_path += "sound/"

        for elem in os.scandir(assets_path):
            if elem.is_dir():
                if elem.name not in current_dict:
                    current_dict[elem.name] = {}

                cls._load_sound(assets_path+elem.name+"/", current_dict[elem.name])

            if elem.is_file():
                key_name = "".join(elem.name.split(".")[:-1])

                if any(elem.name.endswith(ext) for ext in [".wav", ".mp3", ".ogg"]):
                    current_dict[key_name] = pygame.mixer.Sound(assets_path+elem.name)

                else:
                    raise InvalidFileFormatError(f"{elem.name.split('.')[-1]} is not a supported data file format")
