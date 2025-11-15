from functools import reduce


def add(x, y):
    return x + y


result = reduce(lambda x, y: x + y, range(1, 6))
# 1 + 2
# -----
#   3   + 3
# ---------
#    6     + 4
#  -----------
#       10     + 5
#    -------------
#          15
print(result)  # 15

result = reduce(lambda x, y: x * y, range(1, 6))  # factorial 5
1 * 2 * 3 * 4 * 5
# 1 * 2
# -----
#   2   * 3
# ---------
#    6     * 4
#  -----------
#       24     * 5
#    -------------
#          120
print(result)  # 120
