import logging
import re

log = logging.getLogger(__name__)


def cal_multiplication(s: str) -> list[int]:
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return [int(a) * int(b) for (a, b) in pattern.findall(s)]


def part1(s: str) -> int:
    return sum(cal_multiplication(s))


def part2(s: str) -> int:
    return sum(sum(cal_multiplication(part.split("don't")[0])) for part in s.split("do()"))


def parse(data: str) -> str:
    return data.strip()


def solve_part1(data: str) -> int:
    return part1(parse(data))


def solve_part2(data: str) -> int:
    return part2(parse(data))
