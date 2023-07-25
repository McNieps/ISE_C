import random

from ise.environment.entity import Entity
from ise.environment.sprite import SimpleSprite
from ise.environment.position import AdvancedPos
from ise.app.resource import Resource


class CachedSurfEntity(Entity):
    def __init__(self,
                 position: tuple = (200, 200)) -> None:

        position = AdvancedPos(position=position,
                               speed=(random.randint(-10, 10), random.randint(-10, 10)),
                               va=45,
                               a=random.randint(0, 360))

        sprite = SimpleSprite(Resource.image["stock"]["illapsum_splash"])
        sprite.set_rendering_technique("rotated")

        super().__init__(position, sprite)

    def update(self,
               delta: float) -> None:
        super().update(delta)
