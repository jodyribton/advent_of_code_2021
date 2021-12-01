from typing import Iterator


def count_depth_drops(readings: Iterator[int]) -> int:
    """ Given a list of sonar depth readings, count and return the number of times there's a increase in depth. """

    # Take the first reading (if there is one) as our starting point
    try:
        previous_reading: int = next(readings)
    except StopIteration:
        # If there are no values, return 0 (no depth increases)
        return 0

    # Iterate through remaining readings, counting the number of depth increases
    depth_drops: int = 0

    for r in readings:
        if r > previous_reading:
            depth_drops += 1

        previous_reading = r

    return depth_drops


if __name__ == "__main__":
    # Count depth drops in input.txt
    with open('input.txt') as f:
        result = count_depth_drops((int(r) for r in f))

    print("{0} drops in depth in file input.txt".format(result))


def test_count_depth_drops():
    """ Tests for count_depth_drops """

    # An empty list of readings should return 0 drops
    assert count_depth_drops(iter([])) == 0

    # A single item should also return 0 drops
    assert count_depth_drops(iter([9])) == 0

    # Test a list of only depth increases
    drops_only = iter([3, 4, 6, 8, 10])
    assert count_depth_drops(drops_only) == 4

    # Test a list of drops and rises
    bumpy = iter([1, 50, 100, 70, 100, 70])
    assert count_depth_drops(bumpy) == 3
