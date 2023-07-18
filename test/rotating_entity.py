from ise.environment.entity import Entity
from ise.environment.sprite import DebugSprite
from ise.environment.position import AdvancedPos


class MovingEntity(Entity):
    def __init__(self) -> None:
        position = AdvancedPos(va=12)

        super().__init__(position, DebugSprite())

