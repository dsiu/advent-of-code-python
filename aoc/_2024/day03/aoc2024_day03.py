import logging
import re

log = logging.getLogger(__name__)


def cal_multiplication(s: str) -> list[int]:
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    m = mul_pattern.findall(s)
    ret = [int(a) * int(b) for (a, b) in m]
    return ret


def part1(s: str) -> int:
    return sum(cal_multiplication(s))


def part2(s: str) -> int:
    return sum([sum(cal_multiplication(i.split("don't")[0])) for i in s.split("do()")])


def parse(data: str) -> str:
    return data.strip()


def solve_part1(data: str) -> int:
    return part1(parse(data))


def solve_part2(data: str) -> int:
    return part2(parse(data))
