from ise.environment.entity import Entity
from ise.environment.sprite import DebugSprite
from ise.environment.position import StaticPos


class OriginEntity(Entity):
    def __init__(self) -> None:
        super().__init__(StaticPos((0, 0)), DebugSprite())
