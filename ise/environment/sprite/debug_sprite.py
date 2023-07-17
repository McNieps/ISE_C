import ise.environment.location as ise_loc


class DebugSprite:
    def __init__(self,
                 location: type[ise_loc.StaticLoc]) -> None:

        pass


if __name__ == '__main__':
    x = DebugSprite(ise_loc.AdvancedLocation)
