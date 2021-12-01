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


def count_sliding_depth_drops(readings: Iterator[int]) -> int:
    """ Same as count_depth_drops(), but compare sums over a sliding three-value window instead of discrete values."""

    # Take the first three readings as our starting point. If there aren't enough readings, return 0.
    try:
        window_queue = [next(readings), next(readings), next(readings)]
        previous_sum: int = sum(window_queue)
    except StopIteration:
        # If we don't have enough values, return 0 (no depth increases)
        return 0

    # Iterate through remaining readings, counting the number of depth increases
    depth_drops: int = 0

    for r in readings:
        window_queue.pop(0)
        window_queue.append(r)
        new_window_sum = sum(window_queue)

        if new_window_sum > previous_sum:
            depth_drops += 1

        previous_sum = new_window_sum

    return depth_drops


if __name__ == "__main__":
    # Count depth drops in input.txt (Day 1 challenge part 1)
    with open('input.txt') as f:
        simple_depth_drops = count_depth_drops((int(r) for r in f))
    print("{0} drops in depth in file input.txt".format(simple_depth_drops))

    # Count depth drops over a sliding three-reading window (Day 1 challenge part 2)
    with open('input.txt') as f:
        sliding_depth_drops = count_sliding_depth_drops((int(r) for r in f))
    print("{0} drops over three-reading windows in file input.txt".format(sliding_depth_drops))


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


def test_count_sliding_depth_drops():
    """ Tests for count_sliding_depth_drops() """

    # An empty list of readings should return 0 drops
    assert count_sliding_depth_drops(iter([])) == 0

    # A single item should also return 0 drops
    assert count_sliding_depth_drops(iter([9])) == 0

    # 3 items should return 0 drops
    assert count_sliding_depth_drops(iter([9, 10, 9])) == 0

    # Test sliding increases (window sums are 28, 30, 32)
    assert count_sliding_depth_drops(iter([9, 10, 9, 11, 12])) == 2

    # Test sliding increases and decreases (window sums are 28, 30, 21, 24)
    assert count_sliding_depth_drops(iter([9, 10, 9, 11, 1, 12])) == 2
