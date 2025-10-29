# Built-in(No variable):


# sum = 10 # G - Global
def f():
    #  sum = 20 # E - Enclosing
    def g():
        # sum = 30 # L - Local
        print("first var sum in g function Built-in:", sum)  # B - Built-in

    g()
    print("second var sum in f function Built-in:", sum)  # B - Built-in


f()
print("third var sum after g and f function Built-in:", sum)  # B - Built-in

# Local variable only:


# sum = 10
def f():
    #  sum = 20
    def g():
        sum = 30  # L - Local
        print("first var sum in g function Local:", sum)  # Local = 30

    g()
    print("second var sum in f function Local:", sum)  # Built-in


f()
print("third var sum after g and f function Local:", sum)  # Built-in


# Enclosing variable only


# sum = 10 # G - Global
def f():
    sum = 20  # E - Enclosing

    def g():
        # sum = 30  # L - Local
        print("first var sum in g function Enclosing:", sum)  # E - Enclosing = 20

    g()
    print("second var sum in f function Enclosing:", sum)  # E - Enclosing = 20


f()
print("third var sum after g and f function Enclosing:", sum)  # B - Built-in


# Global variable only

sum = 10  # G - Global


def f():
    # sum = 20 # E - Enclosing
    def g():
        # sum = 30  # L - Local
        print("first var sum in g function Global:", sum)  # G - Global = 10

    g()
    print("second var sum in f function Global:", sum)  # G - Global = 10


f()
print("third var sum after g and f function Global:", sum)  # G - Global = 10
