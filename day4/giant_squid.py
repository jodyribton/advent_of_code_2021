""" https://adventofcode.com/2021/day/4 """

from typing import List


class BingoBoard:
    def __init__(self, numbers: List[List[int]]):
        """ Initialise a new 5x5 bingo board with preset numbers """
        self._board_numbers = numbers
        self._board_marked = [[False] * 5, [False] * 5, [False] * 5, [False] * 5, [False] * 5]
        self._past_bingo = False  # A board can only bingo once, subsequent calls take the board out of bingo.

    @property
    def has_bingo(self) -> bool:
        if self._past_bingo is True:
            return False

        """ If any rows or columns of the bingo card are fully marked, this board has bingo. """
        for row in self._board_marked:
            if row == [True] * 5:
                return True

        for column in range(5):
            c = [x[column] for x in self._board_marked]
            if c == [True] * 5:
                return True

        return False

    @property
    def marked_numbers(self) -> List[int]:
        """ All numbers that are currently marked on this board. """

        marked = []
        for y in range(5):
            for x in range(5):
                if self._board_marked[y][x]:
                    marked.append(self._board_numbers[y][x])

        return marked

    @property
    def unmarked_numbers(self) -> List[int]:
        """ All numbers that are currently unmarked on this board. """

        unmarked = []
        for y in range(5):
            for x in range(5):
                if not self._board_marked[y][x]:
                    unmarked.append(self._board_numbers[y][x])

        return unmarked

    def call_number(self, number: int):
        """ Mark number on board (if present) """
        # If this board was in bingo, continuing to play on it makes it invalid.
        if self.has_bingo:
            self._past_bingo = True

        # Find number on the board, and mark it if found.
        for y in range(5):
            for x in range(5):
                if self._board_numbers[y][x] == number:
                    self._board_marked[y][x] = True


def do_challenges():
    bingo_boards = []
    with open('day4/input.txt') as f:
        # First line is a comma-separated list of numbers as they are called
        called_numbers = f.readline()

        # Remainder of the file is a series of 5x5 bingo boards, separated by newlines
        while f.readline():
            new_board = []
            for i in range(5):
                board_line = f.readline()
                numbers = [int(x) for x in board_line.split()]
                new_board.append(numbers)
            bingo_boards.append(BingoBoard(new_board))

    # Start calling numbers, and record our winners.
    winners = []
    for n in called_numbers.split(","):
        for board in bingo_boards:
            board.call_number(int(n))

            if board.has_bingo:
                sum_unmarked = sum(board.unmarked_numbers)
                final_score = sum_unmarked * int(n)
                winners.append([n, final_score])

    print("First bingo winner score: {0}".format(winners[0][1]))
    print("Final bingo winner score: {0}".format(winners[-1][1]))


def test_bingo_board():
    b = BingoBoard([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ])

    assert b.has_bingo is False

    b.call_number(85)
    b.call_number(11)
    assert b.marked_numbers == [11]
    assert b.has_bingo is False

    b.call_number(1)
    b.call_number(6)
    b.call_number(10)
    b.call_number(16)
    b.call_number(21)
    assert b.has_bingo is True
