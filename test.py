from typing import Sequence


def add_numbers(numbers: Sequence[int]) -> int:
    return sum(numbers)


if __name__ == "__main__":
    values = [10, 20, 30]
    print(add_numbers(values))
