import random

from isec.environment.entity import Entity
from isec.environment.sprite import DebugSprite
from isec.environment.position import SimplePos


class MovingEntity(Entity):
    def __init__(self) -> None:
        super().__init__(SimplePos((random.randint(-100, 100),
                                    random.randint(-100, 100)),
                                   (-100, 0)), DebugSprite())

    def update(self,
               delta: float) -> None:

        self.position: SimplePos
        self.position.speed.rotate_ip(180*delta)
        super().update(delta)
