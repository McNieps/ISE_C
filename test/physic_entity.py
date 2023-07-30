from ise.environment import Entity
from ise.environment.position import PymunkPos
from ise.environment.sprite import SimpleSprite
from ise.app.resource import Resource


class PhysicEntity(Entity):
    def __init__(self,
                 position: tuple = (200, 200)) -> None:

        position = PymunkPos(position=position, va=1800)
        position.create_surface_shape(Resource.image["stock"]["face"], radius=-2)

        sprite = SimpleSprite(Resource.image["stock"]["face"], rendering_technique="rotated")

        sprite.set_rendering_technique("rotated")

        super().__init__(position, sprite)

