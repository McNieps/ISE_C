import typing

from isec.app import Resource
from isec.environment import Entity, sprite, position
from isec.instance import BaseInstance


class Button(Entity):
    def __init__(self,
                 button_position: position.Pos = None,
                 button_sprite: sprite.SimpleSprite = None,
                 up_callback: typing.Callable[[], None] = None,
                 down_callback: typing.Callable[[], None] = None,
                 pressed_callback: typing.Callable[[], None] = None) -> None:

        if button_position is None:
            button_position = position.SimplePos()

        if button_sprite is None:
            button_sprite = sprite.SimpleSprite(Resource.image["stock"]["button"],
                                                "static")

        if up_callback is None:
            up_callback = self._empty_callback

        if down_callback is None:
            down_callback = self._empty_callback

        if pressed_callback is None:
            pressed_callback = self._empty_callback

        self.up_callback = up_callback
        self.down_callback = down_callback
        self.pressed_callback = pressed_callback

        self.pressed = False

        super().__init__(button_position, button_sprite)

    def link_to_instance(self,
                         instance: BaseInstance) -> None:

        instance.event_handler.register_buttonup_callback(self.up_callback)
        instance.event_handler.register_buttondown_callback(self.down_callback)
        instance.event_handler.register_buttonpressed_callback(self.pressed_callback)

    def _empty_callback(self):
        return
