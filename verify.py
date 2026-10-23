"""Standalone finite checks for the accompanying mathematical note.

Python 3 standard library only; no file writes, network access or dependencies.
These finite checks do not replace the universal proof in NOTE.md.
"""

from itertools import product


def convolution(a: int, b: int) -> list[int]:
    one_bits_a = [i for i in range(a.bit_length()) if (a >> i) & 1]
    one_bits_b = [j for j in range(b.bit_length()) if (b >> j) & 1]
    digits = [0] * (a.bit_length() + b.bit_length())
    for i in one_bits_a:
        for j in one_bits_b:
            digits[i + j] += 1
    return digits


def weighted_sum(digits: list[int]) -> int:
    return sum(value * (1 << index) for index, value in enumerate(digits))


def normalize(initial: list[int]) -> tuple[int, list[tuple[int, ...]]]:
    current = initial.copy()
    while current and current[-1] == 0:
        current.pop()
    original = weighted_sum(current)
    trace = [tuple(current)]
    for rounds in range(64):
        if all(digit < 2 for digit in current):
            assert weighted_sum(current) == original
            return rounds, trace
        next_digits = [
            (current[j] % 2 if j < len(current) else 0)
            + (current[j - 1] // 2 if j else 0)
            for j in range(len(current) + 1)
        ]
        while next_digits and next_digits[-1] == 0:
            next_digits.pop()
        assert weighted_sum(next_digits) == original
        current = next_digits
        trace.append(tuple(current))
    raise AssertionError("Unexpected absence of stabilization")


def main() -> None:
    checked_pairs = 0
    equalities = 0
    maximum = 0
    for a in range(1, 513):
        for b in range(1, 513):
            initial = convolution(a, b)
            assert weighted_sum(initial) == a * b
            rounds, _ = normalize(initial)
            assert rounds <= max(0, (a * b).bit_length() - 2), (a, b)
            bound = a.bit_length() + b.bit_length() - 2
            assert rounds <= bound, (a, b)
            checked_pairs += 1
            maximum = max(maximum, rounds)
            equalities += int(rounds == bound)

    checked_vectors = 0
    for vector in product(range(5), repeat=6):
        value = weighted_sum(list(vector))
        rounds, _ = normalize(list(vector))
        general_bound = max(0, value.bit_length() - (2 if vector[0] <= 1 else 1))
        assert rounds <= general_bound, (vector, rounds, general_bound)
        checked_vectors += 1

    assert normalize(convolution(3, 3))[1] == [
        (1, 2, 1), (1, 0, 2), (1, 0, 0, 1)
    ]
    assert normalize(convolution(3, 11))[1] == [
        (1, 2, 1, 1, 1),
        (1, 0, 2, 1, 1),
        (1, 0, 0, 2, 1),
        (1, 0, 0, 0, 2),
        (1, 0, 0, 0, 0, 1),
    ]
    assert normalize(convolution(1, 11))[0] == 0
    assert normalize([2])[0] == 1
    assert (checked_pairs, checked_vectors, equalities, maximum) == (262144, 15625, 12, 14)
    print(
        "B1_SYNTHETIC_INDEPENDENT_CONTROL_PASS",
        f"convolution_pairs={checked_pairs}",
        f"general_vectors={checked_vectors}",
        f"bound_equalities={equalities}",
        f"max_rounds={maximum}",
        "negative_control=PASS",
        "worked_traces=PASS",
    )


if __name__ == "__main__":
    main()
