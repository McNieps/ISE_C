import typing
import pygame


class EventHandler:
    def __init__(self):
        self.keypressed_callbacks: dict[int: list[typing.Callable]] = {}

        self.keydown_callbacks: dict[int: list[typing.Callable]] = {}
        self.keyup_callbacks: dict[int: list[typing.Callable]] = {}

        self.buttondown_callbacks: dict[int: list[typing.Callable]] = {}
        self.buttonup_callbacks: dict[int: list[typing.Callable]] = {}
