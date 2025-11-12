def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def power(b: int) -> int:
    def power_inner(a: int) -> int:
        return a**b

    return power_inner


opperations = {
    "add": add,
    "multiply": multiply,
    "power": power,
    "square": power(2),
    "cube": power(3),
}


if __name__ == "__main__":
    # print(opperations["add"](3, 5))
    # print(opperations["multiply"](3, 5))
    # print(opperations["power"](3, 5))
    print(opperations["square"](5))  # 25
    print(opperations["cube"](5))  # 125
