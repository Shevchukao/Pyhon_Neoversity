def mult_by_two(n):  # define a function
    n = n * 2
    return n


a = 3
b = 4
print(
    "mult_by_two var a = 3: ", mult_by_two(a)
)  # a = 3 n = 3 * 2 n = 6 return 6 -> print(6) -> output on screen : 6
print(
    "mult_by_two var b = 4: ", mult_by_two(b)
)  # b = 4 n = 4 * 2 n = 8 return 8 -> print(8) -> output on screen : 8
print(
    "mult_by_two number 3: ", mult_by_two(3)
)  # n = 3 * 2 = 6 return 6 -> print(6) -> -> output on screen : 6
print(
    'mult_by_two string "4": ', mult_by_two("4")
)  # "44", because "4" * 2 = "44" or concatenation "4" + "4"


def mult_by_two_with_negative(n: int) -> int:  # define a function with if statements
    if n < 0:
        n = -n
    n = n * 2
    return n


a = -3
b = -4
print(
    "mult_by_two var negative a = -3: ", mult_by_two_with_negative(a)
)  # a = -3 n = -(-3) n = 3 * 2 n = 6 return 6 -> print(6) -> output on screen : 6
print(
    "mult_by_two var negative b = -4: ", mult_by_two_with_negative(b)
)  # b = -4 n = -(-4) n = 4 * 2 n = 8 return 8 -> print(8) -> output on screen : 8
print(
    "mult_by_two negative number -3: ", mult_by_two_with_negative(-3)
)  # n = -(-3) n = 3 * 2 = 6 return 6 -> print(6) -> -> output on screen : 6


def mul2(m: int | str) -> int | str | None:
    if isinstance(m, int):  # check int type if True -> body
        if m < 0:  # if integer and m < 0
            m = -m  # from negative to positive(modulus)
            m = m * 2  # multiply by 2
        else:  # else if integer and m > 0
            m = m * 2  # multiply by 2
        return m  # return var m int
    if isinstance(m, str):  # check string str type if True -> body
        m = m * 2  # multiply by 2(concatenation string 2 times )
        return m  # return var m str
    return None  # if other types(float or other) -> return None


a = -3
b = 4
c = 4.5
print(mul2(a))
print(mul2(b))
print(mul2(c))
print(mul2("3"))
