f = lambda x, y: x + y


def g(x, y):
    return x + y


print(f(3, 5))  # 8
print(g(3, 5))  # 8
print((lambda x, y: x + y)(3, 5))  # 8

nums = [i for i in range(10)]
print(nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted(nums, key=lambda x: -x))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def f(x):
    return -x


print(sorted(nums, key=f))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
