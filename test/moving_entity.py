import random

from ise.environment.entity import Entity
from ise.environment.sprite import DebugSprite
from ise.environment.position import SimplePos


class MovingEntity(Entity):
    def __init__(self) -> None:
        super().__init__(SimplePos((random.randint(-100, 100), random.randint(-100, 100)),
                                   (-100, 0)), DebugSprite())

    def update(self,
               delta: float) -> None:

        self.position: SimplePos
        self.position.speed.rotate_ip(180*delta)
        super().update(delta)
