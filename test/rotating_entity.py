from ise.environment.entity import Entity
from ise.environment.sprite import DebugSprite
from ise.environment.position import AdvancedPos


class RotatingEntity(Entity):
    def __init__(self) -> None:
        position = AdvancedPos(position=(200, 200), speed=(0, 0), va=45)

        super().__init__(position, DebugSprite())
        self.sprite.set_rendering_technique("rotated")

    def update(self,
               delta: float) -> None:
        super().update(delta)
