from typing import List


def _most_common_in_position(y: int, binary_matrix, default_if_equal: str = "1") -> str:
    # Add all bits in column y in the matrix and check whether the sum > half the height of the matrix.
    y_sum = sum([i[y] for i in binary_matrix])
    half_length = len(binary_matrix) / 2
    if y_sum > half_length:
        most_common_bit = "1"
    elif y_sum == half_length:
        most_common_bit = default_if_equal
    elif y_sum < half_length:
        most_common_bit = "0"

    return most_common_bit


def _least_common_in_position(y: int, binary_matrix, default_if_equal: str = "1") -> str:
    # Add all bits in column y in the matrix and check whether the sum > half the height of the matrix.
    flipped_default = "0" if default_if_equal == "1" else "1"
    most_common_bit = _most_common_in_position(y, binary_matrix, flipped_default)
    least_common_bit = "1" if most_common_bit == "0" else "0"

    return least_common_bit


class Diagnostic:
    def __init__(self, binary_data: List[str]):
        self._binary_matrix = [[int(char) for char in x.strip()] for x in binary_data]

    def _most_common_bits(self) -> str:
        most_common_bits: str = ""
        for y in range(len(self._binary_matrix[0])):
            most_common_bit = _most_common_in_position(y, self._binary_matrix)
            most_common_bits += str(most_common_bit)

        return most_common_bits

    def _least_common_bits(self) -> str:
        least_common_bits = ["1" if i == "0" else "0" for i in self._most_common_bits()]
        return "".join(least_common_bits)

    @property
    def oxygen_generator_rating(self) -> int:
        # Starting from the left, eliminate all numbers that have less-common values in each bit position (keeping
        # values with bit 1 all else b being equal), until we have only one number left.
        remaining_values = self._binary_matrix
        for bit_position in range(len(self._binary_matrix[0])):
            remaining_values = \
                [x for x in remaining_values if x[bit_position] == int(_most_common_in_position(bit_position, remaining_values, "1"))]
            if len(remaining_values) == 1:
                break

        return int("".join([str(x) for x in remaining_values[0]]), 2)

    @property
    def scrubber_rating(self) -> int:
        # Starting from the left, eliminate all numbers that have more-common values in each bit position (keeping
        # values with bit 0 all else b being equal), until we have only one number left.
        remaining_values = self._binary_matrix
        for bit_position in range(len(self._binary_matrix[0])):
            remaining_values = \
                [x for x in remaining_values if
                 x[bit_position] == int(_least_common_in_position(bit_position, remaining_values, "0"))]
            if len(remaining_values) == 1:
                break

        return int("".join([str(x) for x in remaining_values[0]]), 2)

    @property
    def gamma_rate(self) -> int:
        """ The most common bit in every position in the diagnostic data. """
        gamma_rate = int(self._most_common_bits(), 2)
        return gamma_rate

    @property
    def epsilon_rate(self) -> int:
        """ The least common bit in every position in the diagnostic data. """
        epsilon_rate = int(self._least_common_bits(), 2)
        return epsilon_rate

    @property
    def power_consumption(self) -> int:
        return self.gamma_rate * self.epsilon_rate

    @property
    def life_support_rating(self) -> int:
        return self.oxygen_generator_rating * self.scrubber_rating


def do_challenges():
    with open('binary_diagnostic/input.txt') as f:
        binary_data = f.read().splitlines(False)

    d = Diagnostic(binary_data)
    print("Power consumption: {0}".format(d.power_consumption))
    print("Life support rating: {0}".format(d.life_support_rating))


def test_diagnostic():
    t = Diagnostic(["0110", "1001", "1000", "0010"])
    assert t._most_common_bits() == "1010"
    assert t.gamma_rate == 10

    assert t._least_common_bits() == "0101"
    assert t.epsilon_rate == 5

    assert t.power_consumption == 50

    assert _most_common_in_position(2, t._binary_matrix, "0") == "0"
    assert _least_common_in_position(2, t._binary_matrix, "0") == "0"

    assert t.oxygen_generator_rating == 9
    assert t.scrubber_rating == 2
    assert t.life_support_rating == 18


