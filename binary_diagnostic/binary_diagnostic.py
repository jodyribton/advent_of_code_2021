from typing import List


class Diagnostic:
    def __init__(self, binary_data: List[str]):
        self._binary_matrix = [[int(char) for char in x.strip()] for x in binary_data]

    def _most_common_bits(self) -> str:
        most_common_bits: str = ""
        for y in range(len(self._binary_matrix[0])):
            # Add all bits in column y in the matrix and check whether the sum > half the height of the matrix.
            y_sum = sum([i[y] for i in self._binary_matrix])
            most_common_bit = 1 if y_sum > len(self._binary_matrix) / 2 else 0
            most_common_bits += str(most_common_bit)

        return most_common_bits

    def _least_common_bits(self) -> str:
        least_common_bits = ["1" if i == "0" else "0" for i in self._most_common_bits()]
        return "".join(least_common_bits)

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


def do_challenges():
    with open('binary_diagnostic/input.txt') as f:
        binary_data = f.read().splitlines(False)

    d = Diagnostic(binary_data)
    print("Power consumption: {0}".format(d.power_consumption))


def test_diagnostic():
    t = Diagnostic(["0110", "1001", "1000"])
    assert t._most_common_bits() == "1000"
    assert t.gamma_rate == 8

    assert t._least_common_bits() == "0111"
    assert t.epsilon_rate == 7

    assert t.power_consumption == 56


