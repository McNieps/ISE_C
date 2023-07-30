import math
import pygame
import pymunk

from pymunk.autogeometry import march_soft
from collections.abc import Iterable, Sequence

from ise.environment.position.advanced_pos import AdvancedPos


class PymunkPos(AdvancedPos):
    TYPE_DYNAMIC = pymunk.Body.DYNAMIC
    TYPE_KINEMATIC = pymunk.Body.KINEMATIC
    TYPE_STATIC = pymunk.Body.STATIC

    BASE_DENSITY = 10
    BASE_FRICTION = 1.5
    BASE_ELASTICITY = 0.75

    def __init__(self,
                 body_type=TYPE_DYNAMIC,
                 base_shape_density: float = None,
                 base_shape_friction: float = None,
                 base_shape_elasticity: float = None,
                 position: Iterable = None,
                 speed: Iterable = None,
                 accel: Iterable = None,
                 a: float = 0,
                 va: float = 0,
                 aa: float = 0,
                 damping: float = 1,
                 a_damping: float = 1) -> None:

        self.body: pymunk.Body = pymunk.Body(0, 0, body_type=body_type)
        self.shapes: list[pymunk.Shape] = []

        if base_shape_density is None:
            base_shape_density = self.BASE_DENSITY

        if base_shape_friction is None:
            base_shape_friction = self.BASE_FRICTION

        if base_shape_elasticity is None:
            base_shape_elasticity = self.BASE_ELASTICITY

        self.base_shape_density = base_shape_density
        self.base_shape_friction = base_shape_friction
        self.base_shape_elasticity = base_shape_elasticity

        super().__init__(position=position,
                         speed=speed,
                         accel=accel,
                         a=a,
                         va=va,
                         aa=aa,
                         damping=damping,
                         a_damping=a_damping)

    def update(self,
               delta: float) -> None:
        pass

    def set_shape_characteristics(self,
                                  shape: pymunk.Shape,
                                  density: float = None,
                                  friction: float = None,
                                  elasticity: float = None) -> None:

        if density is not None:
            shape.density = density

        elif shape.density == 0:
            shape.density = self.base_shape_density

        if friction is not None:
            shape.friction = friction

        elif shape.friction == 0:
            shape.friction = self.base_shape_friction

        if elasticity is not None:
            shape.elasticity = elasticity

        elif shape.elasticity == 0:
            shape.elasticity = self.base_shape_elasticity

    def add_shape(self,
                  shape: pymunk.Shape,
                  density: float = None,
                  friction: float = None,
                  elasticity: float = None) -> None:

        self.set_shape_characteristics(shape, density, friction, elasticity)
        self.shapes.append(shape)

    def remove_shape(self,
                     shape: pymunk.Shape) -> None:

        self.shapes.remove(shape)

    def create_rect_shape(self,
                          surface: pygame.Surface,
                          _offset: Sequence[float, float] = (0, 0),
                          radius: float = -1,
                          density: float = None,
                          friction: float = None,
                          elasticity: float = None) -> None:

        shape = pymunk.Poly.create_box(self.body, surface.get_size(), radius=radius)
        self.add_shape(shape, density, friction, elasticity)

    def create_surface_shape(self,
                             surface: pygame.Surface,
                             offset: Sequence[float, float] = (0, 0),
                             radius: float = -1,
                             density: float = None,
                             friction: float = None,
                             elasticity: float = None) -> None:

        size = surface.get_size()
        surface_bounding_box = pymunk.BB(0, 0, size[0]-1, size[1]-1)
        surface_array = pygame.surfarray.pixels3d(pygame.mask.from_surface(surface).to_surface())

        def sample_function(_point):
            return surface_array[int(_point[0]), int(_point[1]), 0]

        # First decomposition
        polygons = list(march_soft(surface_bounding_box,
                                   size[0],
                                   size[1],
                                   0.5,
                                   sample_function))

        for i in range(len(polygons)):
            polygon = polygons[i]
            polygons[i] = [(point[0]-size[0]/2+offset[0], point[1]-size[1]/2+offset[1]) for point in polygon]

        shapes = []
        for polygon in polygons:
            bad_poly = pymunk.Poly(body=None, vertices=polygon)
            bad_poly_cog = bad_poly.center_of_gravity
            t = pymunk.Transform(tx=-bad_poly_cog[0], ty=-bad_poly_cog[1])
            shapes.append(pymunk.Poly(self.body, polygon, transform=t, radius=radius))

        for shape in shapes:
            self.add_shape(shape, density, friction, elasticity)

    @property
    def position(self) -> tuple[float, float]:
        return self.body.position

    @position.setter
    def position(self, position: tuple[float, float]) -> None:
        self.body.position = tuple(position)

    @property
    def speed(self) -> tuple[float, float]:
        return self.body.velocity

    @speed.setter
    def speed(self, speed: tuple[float, float]) -> None:
        self.body.velocity = tuple(speed)

    @property
    def a(self) -> float:
        return -math.degrees(self.body.angle)

    @a.setter
    def a(self, a: float) -> None:
        self.body.angle = math.radians(a)

    @property
    def va(self) -> float:
        return -math.radians(self.body.angular_velocity)

    @va.setter
    def va(self, va: float) -> None:
        self.body.angular_velocity = math.radians(va)

    @property
    def aa(self) -> float:
        return self.body.torque

    @aa.setter
    def aa(self, aa: float) -> None:
        self.body.torque = aa

    @property
    def damping(self) -> float:
        return self.body.damping

    @damping.setter
    def damping(self, damping: float) -> None:
        self.body.damping = damping

    @property
    def a_damping(self) -> float:
        return self.body.angular_damping

    @a_damping.setter
    def a_damping(self, a_damping: float) -> None:
        self.body.angular_damping = a_damping


if __name__ == '__main__':
    x = PymunkPos(body_type=PymunkPos.TYPE_KINEMATIC)
