from ise.environment.entity import Entity
from ise.environment.sprite import SimpleSprite
from ise.environment.position import AdvancedPos
from ise.app.resource import Resource


class CachedSurfEntity(Entity):
    def __init__(self) -> None:
        position = AdvancedPos(position=(200, 200), speed=(1, 0), va=45)

        sprite = SimpleSprite(Resource.image["stock"]["arrow"])
        sprite.set_rendering_technique("cached")

        super().__init__(position, sprite)

    def update(self,
               delta: float) -> None:
        super().update(delta)
