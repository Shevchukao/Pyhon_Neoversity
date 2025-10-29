def add(a, *args):
    print("tuple:", args)  # tuple without a (3,4,5,6)
    return args  # return args


print("Function input add(2,3,4,5,6) output (3,4,5,6):", add(2, 3, 4, 5, 6))


def add1(
    a, *args, b=6
):  # defenition function with (a argument), and some *args tuple type
    sum = a + b  # if only one element a
    if (
        len(args) > 0
    ):  # if statement for lenght args more 0  # we can deleted this compare
        for value in args:  # loops with var value = elements tuple
            sum += value  # a + all element args

    return sum  # return sum


print("Sum element a and *args and default b:", add1(2, 3, 4, 5, 6))
print("Sum element a and *args and named b:", add1(2, 3, 4, 5, 6, b=8))


def add2(a, *args, b=6):  # named parameter after *args, (first b)
    sum = a + b  # if only one element a
    if (
        len(args) > 0
    ):  # if statement for lenght args more 0  # we can deleted this compare
        for value in args:  # loops with var value = elements tuple
            sum += value  # a + all element args
        # b = 10  # (third b)
    return sum, b  # return (sum and b) in tuple because two argument


print("Sum element a and *args and default b in tuple:", add2(2, 3, 4, 5, 6))
print(
    "Sum element a and *args and named b in tuple:", add2(2, 3, 4, 5, 6, b=8)
)  # (second b)


def add3(
    a, *args, b=6, **kwargs
):  # (positions, any position = *args(tuple), named, **kwargs(dictionary)) parameters
    sum = a + b  # if only one element a
    print("dictionary:", kwargs)  # dictionary
    if (
        len(args) > 0
    ):  # if statement for lenght args more 0  # we can deleted this compare
        for value in args:  # loops with var value = elements tuple
            sum += value  # a + all element args
    return sum, b, kwargs  # return (sum and b) in tuple because two argument


print(
    "Sum element a and *args and named b in tuple:",
    add3(2, 3, 4, 5, 6, b=8, server="google.com", port=1033),
)


def add3(a, *args, **kwargs):
    sum = a
    if len(args) > 0:
        for value in args:
            sum += value
    return sum, kwargs


print(
    "Sum element a and *args and dictionary with three key-value:",
    add3(2, 3, 4, 5, 6, b=8, server="google.com", port=1033),
)
