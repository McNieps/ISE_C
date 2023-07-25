import pygame
import typing


class EventHandler:
    def __init__(self) -> None:
        self._keypressed_callbacks: dict[int, list[typing.Callable]] = {}
        self._keydown_callbacks: dict[int, list[typing.Callable]] = {}
        self._keyup_callbacks: dict[int, list[typing.Callable]] = {}

        self._buttonpressed_callbacks: dict[int, list[typing.Callable]] = {}
        self._buttondown_callbacks: dict[int, list[typing.Callable]] = {}
        self._buttonup_callbacks: dict[int, list[typing.Callable]] = {}

        self._quit_callbacks: list[typing.Callable] = []

    def register_keypressed_callback(self,
                                     key: int,
                                     callback: typing.Callable) -> None:
        """Registers a callback to be called when the key is pressed."""

        if key not in self._keypressed_callbacks:
            self._keypressed_callbacks[key] = []
        self._keypressed_callbacks[key].append(callback)

    def register_keydown_callback(self,
                                  key: int,
                                  callback: typing.Callable) -> None:
        """Registers a callback to be called when the key is down."""

        if key not in self._keydown_callbacks:
            self._keydown_callbacks[key] = []
        self._keydown_callbacks[key].append(callback)

    def register_keyup_callback(self,
                                key: int,
                                callback: typing.Callable) -> None:
        """Registers a callback to be called when the key is up."""
        if key not in self._keyup_callbacks:
            self._keyup_callbacks[key] = []
        self._keyup_callbacks[key].append(callback)

    def register_buttondown_callback(self,
                                     button: int,
                                     callback: typing.Callable) -> None:
        """Registers a callback to be called when the button is down."""
        if button not in self._buttondown_callbacks:
            self._buttondown_callbacks[button] = []
        self._buttondown_callbacks[button].append(callback)

    def register_buttonup_callback(self,
                                   button: int,
                                   callback: typing.Callable) -> None:
        """Registers a callback to be called when the button is up."""
        if button not in self._buttonup_callbacks:
            self._buttonup_callbacks[button] = []
        self._buttonup_callbacks[button].append(callback)

    def register_quit_callback(self,
                               callback: typing.Callable) -> None:
        """Registers a callback to be called when the game is quit."""
        self._quit_callbacks.append(callback)

    def _keypressed(self,
                    key: int) -> None:
        """Calls all callbacks registered to the key pressed."""
        for callback in self._keypressed_callbacks[key]:
            callback()

    def _keydown(self,
                 key: int) -> None:
        """Calls all callbacks registered to the key down."""
        for callback in self._keydown_callbacks[key]:
            callback()

    def _keyup(self,
               key: int) -> None:
        """Calls all callbacks registered to the key leave."""
        for callback in self._keyup_callbacks[key]:
            callback()

    def _buttonpressed(self,
                       button: int) -> None:
        """Calls all callbacks registered to the button pressed."""
        for callback in self._buttonpressed_callbacks[button]:
            callback()

    def _buttondown(self,
                    button: int) -> None:
        """Calls all callbacks registered to the button down."""
        for callback in self._buttondown_callbacks[button]:
            callback()

    def _buttonup(self,
                  button: int) -> None:
        """Calls all callbacks registered to the button up."""
        for callback in self._buttonup_callbacks[button]:
            callback()

    def _quit(self) -> None:
        """Calls all callbacks registered to the quit event."""
        for callback in self._quit_callbacks:
            callback()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
                continue

            if event.type == pygame.KEYDOWN:
                self._keydown(event.key)
                continue

            if event.type == pygame.KEYUP:
                self._keyup(event.key)
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._buttondown(event.button)
                continue

            if event.type == pygame.MOUSEBUTTONUP:
                self._buttonup(event.button)
                continue

        key_pressed = pygame.key.get_pressed()
        button_pressed = pygame.mouse.get_pressed(5)

        for key in self._keypressed_callbacks:
            if key_pressed[key]:
                self._keypressed(key)

        for button in self._buttonpressed_callbacks:
            if button_pressed[button]:
                self._buttonpressed(button)
