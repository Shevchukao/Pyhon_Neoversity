import time


def decorator(func):
    def inner_function(*args, **kwargs):
        print(f"Function: {func.__name__} with parameter: {args}, {kwargs}")
        print(f"at {time.time()}")
        result = func(*args, **kwargs)
        print(f"Result {result}")
        print(f"Function finished at {time.time()}")
        return result

    return inner_function


@decorator
def add(x, y):
    return x + y


if __name__ == "__main__":

    print(add(1, 2))
