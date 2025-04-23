import logging

log = logging.getLogger(__name__)


def parse(data: str) -> list[list[int]]:
    lines = [line.strip().split("   ") for line in data.strip().split("\n")]
    return [list(map(int, i)) for i in zip(*lines, strict=False)]


def part1(l1: list[int], l2: list[int]) -> int:
    return sum([abs(a - b) for (a, b) in zip(sorted(l1), sorted(l2), strict=False)])


def part2(l1: list[int], l2: list[int]) -> int:
    return sum([a * l2.count(a) for a in l1])


def solve_part1(data: str) -> int:
    [l1, l2] = parse(data)
    return part1(l1, l2)


def solve_part2(data: str) -> int:
    [l1, l2] = parse(data)
    return part2(l1, l2)
