import logging
from typing import Callable

log = logging.getLogger(__name__)

type Report = list[int]
type Reports = list[map[int]]

is_inc = lambda diffs: all(x > 0 for x in diffs)
is_dec = lambda diffs: all(x < 0 for x in diffs)
is_diff_min_one = lambda diffs: all(abs(x) >= 1 for x in diffs)
is_diff_max_three = lambda diffs: all(abs(x) <= 3 for x in diffs)


def diff(x: int, y: int) -> int:
    return y - x


def is_safe(report: Report) -> bool:
    diffs = [diff(x, y) for (x, y) in zip(report[:-1], report[1:])]

    return (is_inc(diffs) or is_dec(diffs)) and is_diff_min_one(diffs) and is_diff_max_three(diffs)


def is_safe_with_tolerance(report: Report) -> bool:
    if is_safe(report):
        return True
    else:
        sub_reports = [report[:i] + report[i + 1 :] for i in range(len(report))]
        return any(is_safe(r) for r in sub_reports)


def count_cond_met(reports: Reports, cond: Callable[[Report], bool]) -> int:
    return len([r for r in reports if cond(list(r))])


def part1(reports: Reports) -> int:
    return count_cond_met(reports, is_safe)


def part2(reports: Reports) -> int:
    return count_cond_met(reports, is_safe_with_tolerance)


def parse(data: str) -> Reports:
    return [map(int, line.split(" ")) for line in data.strip().splitlines()]


def solve_part1(data: str) -> int:
    return part1(parse(data))


def solve_part2(data: str) -> int:
    return part2(parse(data))
