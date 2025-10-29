def f():  # first function
    return "f"


def g():  # second function
    return "g"


def h(x):  # function in
    print(f"function:", x())


x = f
y = g
h(x)  # call outer function h with inner function f
h(y)  # call outer function h with inner function g
