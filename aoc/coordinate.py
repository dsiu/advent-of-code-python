type t = tuple[int, int]


class Direction:
    @staticmethod
    def north(c: t) -> t:
        return c[0], c[1] - 1

    @staticmethod
    def east(c: t) -> t:
        return c[0] + 1, c[1]

    @staticmethod
    def south(c: t) -> t:
        return c[0], c[1] + 1

    @staticmethod
    def west(c: t) -> t:
        return c[0] - 1, c[1]

    @staticmethod
    def northeast(c: t) -> t:
        return Direction.east(Direction.north(c))

    @staticmethod
    def northwest(c: t) -> t:
        return Direction.west(Direction.north(c))

    @staticmethod
    def southeast(c: t) -> t:
        return Direction.east(Direction.south(c))

    @staticmethod
    def southwest(c: t) -> t:
        return Direction.west(Direction.south(c))


class StepFunctions:
    @staticmethod
    def stepN(c: t) -> t:
        return Direction.north(c)

    @staticmethod
    def stepE(c: t) -> t:
        return Direction.east(c)

    @staticmethod
    def stepS(c: t) -> t:
        return Direction.south(c)

    @staticmethod
    def stepW(c: t) -> t:
        return Direction.west(c)

    @staticmethod
    def stepNE(c: t) -> t:
        return Direction.northeast(c)

    @staticmethod
    def stepNW(c: t) -> t:
        return Direction.northwest(c)

    @staticmethod
    def stepSE(c: t) -> t:
        return Direction.southeast(c)

    @staticmethod
    def stepSW(c: t) -> t:
        return Direction.southwest(c)
