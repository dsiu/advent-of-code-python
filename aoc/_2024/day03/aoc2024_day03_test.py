from .aoc2024_day03 import solve_part1, solve_part2
from .data import data, sample_data, sample_data2


# Test Part 1
def test_part1() -> None:
    # Test with sample data
    assert solve_part1(sample_data) == 161
    # Test with actual data
    assert solve_part1(data) == 182780583


# Test Part 2
def test_part2() -> None:
    # Test with sample data
    assert solve_part2(sample_data2) == 48
    # Test with actual data
    assert solve_part2(data) == 90772405
