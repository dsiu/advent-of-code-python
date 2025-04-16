from .aoc2024_dayXX import solve_part1, solve_part2
from .data import data, sample_data


# Test Part 1
def test_part1() -> None:
    # Test with sample data
    assert solve_part1(sample_data) == 1
    # Test with actual data
    assert solve_part1(data) == 1


# Test Part 2
def test_part2() -> None:
    # Test with sample data
    assert solve_part2(sample_data) == 2
    # Test with actual data
    assert solve_part2(data) == 2
