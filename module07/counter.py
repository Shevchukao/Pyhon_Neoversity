from collections import Counter

marks = [2, 4, 5, 2, 3, 1, 4, 5, 4, 3, 5, 4, 3, 3, 5, 5]
marks_counter = Counter(marks)
print(marks_counter)  # Counter({5: 5, 4: 4, 3: 4, 2: 2, 1: 1})
print(marks_counter.most_common(1))  # [(5, 5)]
print(marks_counter.most_common(2))  # [(5, 5), (4, 4)]
print(Counter([1, 2]))  # Counter({1: 1, 2: 1})
print(
    Counter("Hello World")  # .most_common(1) [('l', 3), ('o', 2)]
)  # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
print(
    Counter("some text is log, some is short, but long and short are not some".split())
)  # Counter({'some': 3, 'is': 2, 'text': 1, 'log,': 1, 'short,': 1, 'but': 1, 'long': 1, 'and': 1, 'short': 1, 'are': 1, 'not': 1})
