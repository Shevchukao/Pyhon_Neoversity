numbers = [i for i in range(1, 11)]
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(map(lambda x: x * x, numbers))
print(numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def f(n):
    return "0" + str(n)


numbers = list(map(f, range(1, 11)))
print(numbers)  # ['01', '02', '03', '04', '05', '06', '07', '08', '09', '010']
