a = 5
b = 3
c = 4
print("a:", a, "b:", b, "c:", c)
r = a > 5
print("a > 5: ", r)  # 5 not greater than 5 -> False

d = (True or False) and (True and True)
print(
    "(True or False) and (True and True): ", d
)  # using always round brackets for logical operators with complex expressions

s = (a > 5) & (
    b < 4
)  # & == AND, [TRUE & TRUE == TRUE] [TRUE & FALSE == FALSE] [FALSE & TRUE == FALSE] [FALSE & FALSE == FALSE]
print("(a > 5) & (b < 4): ", s)
t = (a > 5) and (
    b < 4
)  # AND == &, [TRUE AND TRUE == TRUE] [TRUE AND FALSE == FALSE] [FALSE AND TRUE == FALSE] [FALSE AND FALSE == FALSE]
print("(a > 5) and (b < 4): ", t)

p = (a > 5) | (
    b < 4
)  # | == OR, [TRUE | TRUE == TRUE] [TRUE | FALSE == TRUE] [FALSE | TRUE == TRUE] [FALSE | FALSE == FALSE]
print("(a > 5) | (b < 4): ", p)
q = (a > 5) or (
    b < 4
)  # OR == |, [TRUE OR TRUE == TRUE] [TRUE OR FALSE == TRUE] [FALSE OR TRUE == TRUE] [FALSE OR FALSE == FALSE]
print("(a > 5) or (b < 4): ", q)

o = (a > 5) ^ (
    b < 4
)  # XOR == ^, [TRUE ^ TRUE == FALSE] [TRUE ^ FALSE == TRUE] [FALSE ^ TRUE == TRUE] [FALSE ^ FALSE == FALSE]
print("(a > 5) ^ (b < 4): ", o)  # XOR == water is only cold or hot, we don't have warm

u = not (a > 5)  # [NOT TRUE == FALSE] [NOT FALSE == TRUE]
print("not (a > 5): ", u)
v = not a > 5  # [NOT TRUE == FALSE] [NOT FALSE == TRUE]
print("not a > 5: ", v)

w = b < c < a  # equivalent w = (b < c) and (c < a)
print("b < c < a == (b < c and c < a): ", w)

x = b > c < a  # equivalent w = (b > c) and (c < a)
print("b > c < a == (b > c and c < a): ", x)
