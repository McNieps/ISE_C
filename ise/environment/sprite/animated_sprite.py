import pygame

from ise.environment.sprite.simple_sprite import SimpleSprite


class AnimatedSprite(SimpleSprite):
    def __init__(self,
                 surfaces: list[pygame.Surface],
                 frame_durations: list[float],
                 loop: bool = True) -> None:

        super().__init__(surfaces[0])

        self.surfaces: list[pygame.Surface] = surfaces
        self.frame_durations: list[float] = frame_durations
        self.loop: bool = loop

        self._current_frame: int = 0
        self._current_duration: float = 0.0

    def update(self,
               delta: float) -> None:

        self._current_duration += delta

        if self._current_duration >= self.frame_durations[self._current_frame]:
            self._current_frame += 1
            self._current_duration = self._current_duration - self.frame_durations[self._current_frame - 1]

            if self._current_frame >= len(self.surfaces):
                if self.loop:
                    self._current_frame = 0
                else:
                    self._current_frame = len(self.surfaces) - 1

    def render(self,
               destination: pygame.Surface,
               destination_rect: pygame.Rect,
               offset: tuple[int, int],
               angle: float) -> None:

        self.surface = self.surfaces[self._current_frame]
        super().render(destination, destination_rect, offset, angle)
