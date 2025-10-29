# Change Global -> Enclosing because global:

sum = 10  # G - Global -> Enclosing


def f():
    global sum
    sum = 20  # E -> G - Enclosing -> Global

    def g():
        sum = 30  # L - Local
        print("first var sum in g function Enclosing -> Global:", sum)  # L = 30

    g()
    print(
        "second var sum in f function Enclosing -> Global:", sum
    )  # E -> G - Enclosing -> Global = 20


f()
print(
    "third var sum after g and f function Enclosing -> Global:", sum
)  # E -> G - Enclosing -> Global = 20


# Change Local -> Non Local because nonlocal:


sum = 10  # G - Global


def f():
    sum = 20  # E -> NonL - Enclosing -> Non Local

    def g():
        nonlocal sum
        sum = 30  # L -> NonL - Local -> Non Local
        print("first var sum in g function Enclosing -> Local:", sum)  # L = 30

    g()
    print(
        "second var sum in f function Enclosing -> Local:", sum
    )  # E -> L - Enclosing -> Local = 30


f()
print(
    "third var sum after g and f function Enclosing -> Local:", sum
)  # G - Global = 10
