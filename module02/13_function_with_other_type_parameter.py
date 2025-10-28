# Function with two parameter
def add(a, b):  # parameter a, b of function add
    return a + b  # return result


print(
    "For add use parameter a and b, without default: ", add(2, 3)
)  # position arguments: 2 and 3


# Function with two parameter but second have default value:
# parameter a(hasn't default argument), b(has default argument) of function add
def add1(a, b=3):
    return a + b  # return result


# position argument: 2 only and default argument from function 3
print("For add use only parameter a, by default b(default argument): ", add1(2))


def add2(a, b):
    return a + b  # return result


# named argument a = 2 and b = 3
print("For add use only parameter a, by default b(named argument): ", add2(b=3, a=2))

# def add1(a, b=3, c): # not correct, because c need to be on second place befor non positional arguments
# def add1(a, c, b=3): # correct, because position argument c before default parameters
#    return a + b  # return result
