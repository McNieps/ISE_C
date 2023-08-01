from isec.environment import Entity
from isec.environment.position import PymunkPos
from isec.environment.sprite import AnimatedSprite
from isec.environment.sprite.pymunk_sprite import PymunkSprite
from isec.app.resource import Resource


class PhysicEntity(Entity):
    def __init__(self,
                 position: tuple = (200, 200)) -> None:

        position = PymunkPos(position=position, va=0, base_shape_friction=0.5, base_shape_elasticity=0.4)
        position.create_surface_shape(Resource.image["stock"]["face"], radius=0)

        real_surf = Resource.image["stock"]["face"]
        pymunk_surf = PymunkSprite(position, "static").surface

        sprite = AnimatedSprite([real_surf, pymunk_surf], "rotated", [0.1, 0.1])

        super().__init__(position, sprite)
