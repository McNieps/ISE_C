import pygame
import pymunk
import typing

from ise.environment.sprite.simple_sprite import SimpleSprite
from ise.environment.position.pymunk_pos import PymunkPos


class PymunkSprite(SimpleSprite):
    def __init__(self,
                 pymunk_pos: PymunkPos,
                 rendering_technique: typing.Literal["static", "rotated", "cached"]) -> None:

        if len(pymunk_pos.shapes) == 0:
            raise ValueError("PymunkPos must have at least one shape")

        bb_min_x = min([shape.bb.left for shape in pymunk_pos.shapes])
        bb_min_y = min([shape.bb.bottom for shape in pymunk_pos.shapes])
        bb_max_x = max([shape.bb.right for shape in pymunk_pos.shapes])
        bb_max_y = max([shape.bb.top for shape in pymunk_pos.shapes])

        surface = pygame.Surface((bb_max_x - bb_min_x, bb_max_y - bb_min_y))

        for shape in pymunk_pos.shapes:
            if isinstance(shape, pymunk.Circle):
                pygame.draw.circle(surface,
                                   (255, 255, 255),
                                   shape.body.position - (bb_min_x, bb_min_y),
                                   shape.radius)

            if isinstance(shape, pymunk.Segment):
                pygame.draw.line(surface,
                                 (255, 255, 255),
                                 shape.a - (bb_min_x, bb_min_y),
                                 shape.b - (bb_min_x, bb_min_y))

            if isinstance(shape, pymunk.Poly):
                pygame.draw.polygon(surface,
                                    (255, 255, 255),
                                    shape.get_vertices())

            else:
                raise TypeError(f"Unknown shape type: {type(shape)}")

        super().__init__(surface,
                         rendering_technique)
