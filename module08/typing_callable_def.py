# from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


# Theory
# def apply_opperations(a: int, b: int, op: Callable[[int, int], int]) -> int:
#    return op(a, b)


# Practical
def apply_opperations(a: int, b: int, op) -> int:
    return op(a, b)


if __name__ == "__main__":
    print(apply_opperations(3, 5, add))
    print(apply_opperations(3, 5, multiply))
