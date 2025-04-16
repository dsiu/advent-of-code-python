import logging
import sys
import time

from .aoc2024_dayXX import solve_part1, solve_part2
from .data import sample_data

log = logging.getLogger(__name__)


def main() -> None:
    print(sys.path)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    # Running Part 1
    startTimePart1 = time.perf_counter()

    part1 = solve_part1(sample_data)
    # part1 = solvePart1(data)

    endTimePart1 = time.perf_counter()

    log.info("Part 1 Result")
    log.info(part1)
    log.info(f"Part 1 Time: {endTimePart1 - startTimePart1:10.4e} seconds")

    log.info("----------")

    # Running Part 2
    startTimePart2 = time.perf_counter()

    part2 = solve_part2(sample_data)
    # part2 = solvePart2(data)

    endTimePart2 = time.perf_counter()

    log.info("Part 2 Result")
    log.info(part2)
    log.info(f"Part 2 Time: {endTimePart2 - startTimePart2:10.4e} seconds")


if __name__ == "__main__":
    main()
