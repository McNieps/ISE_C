from collections.abc import Iterable


class Pos:
    """
    An abstract position class
    """

    __slots__ = ["position", "speed", "accel", "damping", "a", "va", "aa", "a_damping"]

    def __init__(self,
                 position: Iterable = None,
                 speed: Iterable = None,
                 accel: Iterable = None,
                 damping: float = 1,
                 a: float = 0,
                 va: float = 0,
                 aa: float = 0,
                 a_damping: float = 1) -> None:

        self.position = position
        self.speed = speed
        self.accel = accel
        self.damping = damping

        self.a = a
        self.va = va
        self.aa = aa
        self.a_damping = a_damping
