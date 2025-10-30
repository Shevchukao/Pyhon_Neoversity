import math  # import module math but we need use math.pi, math.trunc and other
from decimal import Decimal  # import module for correct math operations

# from math import *  # it's not correct, import module math but we need use pi, trunc without math. (first e constant with module math)
# from someothermodule import e # using module e from this not from math (second e constant with module someothermodule)
# e = "escape"  # it's bad because e is (third e constant in module math and e will be "escape" not from math or someothermodule)

print(
    "constants: pi, e, inf, nan:", math.pi, math.e, math.inf, math.nan
)  # we have access to constant in code
print("sin pi/2 math.sin(math.pi / 2):", math.sin(math.pi / 2))
print("sin pi math.sin(math.pi):", math.sin(math.pi))  # != 0 by default
print("cos pi math.cos(math.pi):", math.cos(math.pi))  # -1.0 no problem

print("3e5 == 3*10**5 :", 3e5 == 3 * 10**5)  # 3e5 == 3*10**5, True
# 3e5  number 3 is mantissa, letter e exponent, which means multiplied by 10 to the power of, number 5 is exponent
# 1/10 1/2*5 (5 is not a factor of the binary system's base, 2) (-1)^sign * 2^(exponent-bias) * (1+fraction) This structure allows the 64-bit floating-point number
# to represent a vast range of values, from approximately 10^-308 to 10^308, with around 15–17 decimal digits of precision.

# IEEE 754      sign bit(S) 1/1 bit         exponent(E) 8/11bits                                        mantissa or fraction (F) 23/52bits
# 1             positive / negative    bits that indicate (the power of 2)                     bits for represent the precision of the number
# 32 bits             0 - 1                  00000000 - 11111111                              00000000000000000000000 - 11111111111111111111111
# 64 bits             0 - 1               00000000000 - 11111111111        0000000000000000000000000000000000000000000000000000 - 1111111111111111111111111111111111111111111111111111
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)  # False, because IEEE 754 and i8087
# 123*2**10==1024*123==125952

print(
    "math.sin(math.pi) == 0:", math.sin(math.pi) == 0
)  # False, but we need will be True
print(
    "close number left 0.1 + 0.2 with number right 0.3 -> Bool math.isclose(0.1 + 0.2, 0.3):",
    math.isclose(0.1 + 0.2, 0.3),
)  # determine closes number for float number and other number, result is True

print(
    "Greatest Common Divisor 15, 12 math.gcd(15, 12):", math.gcd(15, 12)
)  # Greatest Common Divisor for 15 12 -> 3

print(
    "correct 0.2 + 0.1 using string and decimal module:",
    Decimal("0.2") + Decimal("0.1"),
)  # for correct math operations use module Decimal using number in format string

n = 3.25
print(
    "round number with cound ndigits after dot round(3.335,1):", round(3.335, 1)
)  # round number
print("round up to int number math.ceil(n):", math.ceil(n))  # round in up int number
print(
    "round down to int number math.floor(n):", math.floor(n)
)  # round in down int number
print(
    "round to int number delete number after dot math.trunc(n):", math.trunc(n)
)  # round int number delete float part number after dot

# 3^x=9 a^x=b
# x=log3(9) x=loga(b)
x = math.log(9, 3)  # x = 9 end result, base of number = 3, x number after **
print("log3(9) == 2 math.log(9, 3):", x)  # 2.0
print("contant e math.e:", math.e)
x = math.log(9)  # x = 9 end result -> x=loge(9) -> x=ln(9) e^x=9 2.718^x=9
print("log(9)/ln(9) == 2.197 math.log(9):", x)  # ln(x) = 2.197
# exp(3) == e^3
print(
    "e^(4*loge(2)) == 16 math.exp(4*math.log(2)):", round(math.exp(4 * math.log(2)))
)  # e^(4*loge(2)) == 16

print(
    "2**4 == 16 math.pow(2,4) == 16.0:", math.pow(2, 4)
)  # float pow(2,4) == int/float 2**4
print(
    "4**0.5 == 2 math.sqrt(4) == 2.0:", math.sqrt(4)
)  # float sqrt4 == int/float 4**0.5
