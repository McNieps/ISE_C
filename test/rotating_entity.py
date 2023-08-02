from isec.environment.base.entity import Entity
from isec.environment.sprite import DebugSprite
from isec.environment.position import AdvancedPos


class RotatingEntity(Entity):
    def __init__(self) -> None:
        position = AdvancedPos(position=(200, 200), speed=(0, 0), va=45)

        super().__init__(position, DebugSprite())

    def update(self,
               delta: float) -> None:
        super().update(delta)
