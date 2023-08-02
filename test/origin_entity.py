from isec.environment.base.entity import Entity
from isec.environment.sprite import DebugSprite
from isec.environment.position import StaticPos


class OriginEntity(Entity):
    def __init__(self) -> None:
        super().__init__(StaticPos((0, 0)), DebugSprite())
