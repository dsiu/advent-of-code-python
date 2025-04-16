import logging

log = logging.getLogger(__name__)


def parse(data: str) -> list[int]:
    lines = [int(line) for line in data.strip().split("\n")]
    return lines


def solve_part1(data: str) -> int:
    return 1


def solve_part2(data: str) -> int:
    return 2
