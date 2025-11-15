def log(func):
    def inner(*args, **kwargs):
        with open("log1.txt", "a") as f:
            f.write(f"{func.__name__}({args}{kwargs})\n")

        return func(*args, **kwargs)

    return inner


@log
def add(a, b):
    return a + b


@log
def mult(a, b):
    return a * b


@log
def sub(a, b):
    return a - b


if __name__ == "__main__":
    add(1, 2)
    add(2, 3)
    mult(3, 5)
    sub(4, 5)
