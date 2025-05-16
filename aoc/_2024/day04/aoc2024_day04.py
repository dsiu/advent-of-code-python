import logging
from collections.abc import Callable

import aoc.coordinate as coord

StepFn = coord.StepFunctions

log = logging.getLogger(__name__)


def point_extensions(steps: int) -> Callable[[coord.t], list[list[coord.t]]]:
    def ret_f(start_pos: coord.t) -> list[list[coord.t]]:
        directions = [
            StepFn.stepNW,
            StepFn.stepN,
            StepFn.stepNE,
            StepFn.stepW,
            StepFn.stepE,
            StepFn.stepSW,
            StepFn.stepS,
            StepFn.stepSE,
        ]

        def loop(acc: list[coord.t], cur: coord.t, i: int, f: Callable[[coord.t], coord.t]) -> list[coord.t]:
            next_ = f(cur)
            if i >= steps - 1:
                return acc
            else:
                return loop([*acc, next_], next_, i + 1, f)

        return [loop([start_pos], start_pos, 0, f) for f in directions]

    return ret_f


def x_extension(c: coord.t) -> list[list[coord.t]]:
    return [[c, StepFn.stepNW(c), StepFn.stepNE(c), StepFn.stepSW(c), StepFn.stepSE(c)]]


def potential_words(exts: Callable[[coord.t], list[list[coord.t]]], grid: list[list[str]]) -> list[list[coord.t]]:
    return [word for y, row in enumerate(grid) for x, _ in enumerate(row) for word in exts((x, y))]


def valid_words(words: list[list[coord.t]], grid: list[list[str]]) -> list[list[coord.t]]:
    len_y = len(grid)
    len_x = len(grid[0])

    def is_valid_xy(xy: coord.t) -> bool:
        x, y = xy
        return 0 <= x < len_x and 0 <= y < len_y

    valid_word = lambda word: all(is_valid_xy(xy) for xy in word)

    return [word for word in words if valid_word(word)]


def found_words(words: list[list[coord.t]], grid: list[list[str]]) -> list[str]:
    return ["".join(grid[y][x] for x, y in word) for word in words]


def is_xmas(word: str) -> bool:
    return word == "AMMSS" or word == "ASMSM" or word == "AMSMS" or word == "ASSMM"


def part2(grid: list[list[str]]) -> int:
    return len([x for x in found_words(valid_words(potential_words(x_extension, grid), grid), grid) if is_xmas(x)])


def part1(grid: list[list[str]], word: str) -> int:
    return len([
        w for w in found_words(valid_words(potential_words(point_extensions(4), grid), grid), grid) if w == word
    ])


def parse(data: str) -> list[list[str]]:
    lines = [list(line) for line in data.strip().split("\n")]
    return lines


def solve_part1(data: str) -> int:
    return part1(parse(data), "XMAS")


def solve_part2(data: str) -> int:
    return part2(parse(data))
