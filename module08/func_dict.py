def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(a: int, b: int) -> int:
    return a**b


opperations = {"add": add, "multiply": multiply, "power": power}


if __name__ == "__main__":
    print(opperations["add"](3, 5))
    print(opperations["multiply"](3, 5))
    print(opperations["power"](3, 5))
