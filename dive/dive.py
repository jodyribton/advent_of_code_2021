""" Advent of Code 2021 day 2 challenge

 https://adventofcode.com/2021/day/2
 """


class Sub:
    def __init__(self):
        self._horizontal_position: int = 0
        self._depth: int = 0

    @property
    def horizontal_position(self):
        return self._horizontal_position

    @property
    def depth(self):
        return self._depth

    def instruct(self, command: str):
        (direction, distance) = command.split()
        distance = int(distance)

        if direction == "forward":
            self._horizontal_position += distance
        elif direction == "down":
            self._depth += distance
        elif direction == "up":
            self._depth -= distance
        else:
            print("Unexpected command {0}".format(direction))


class AimedSub(Sub):
    def __init__(self):
        super().__init__()
        self._aim: int = 0

    def instruct(self, command: str):
        (direction, distance) = command.split()
        distance = int(distance)

        if direction == "forward":
            self._horizontal_position += distance
            self._depth += self._aim * distance
        elif direction == "down":
            self._aim += distance
        elif direction == "up":
            self._aim -= distance
        else:
            print("Unexpected command {0}".format(direction))


def do_challenges():
    with open('dive/input.txt') as f:
        sub = Sub()
        for r in f:
            sub.instruct(r)
    print("Basic submarine ends in position {0} with depth {1} (product {2})".format(
        sub.horizontal_position, sub.depth, sub.horizontal_position * sub.depth))

    with open('dive/input.txt') as f:
        aimed_sub = AimedSub()
        for r in f:
            aimed_sub.instruct(r)
    print("Aimed submarine ends in position {0} with depth {1} (product {2})".format(
        aimed_sub.horizontal_position, aimed_sub.depth, aimed_sub.horizontal_position * aimed_sub.depth))


