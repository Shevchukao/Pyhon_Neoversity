from collections import defaultdict


string = "some text is log, some is short, but long and short are not some"
# OLD SLOW AND BORING WAY
# dict = {}

# for letter in string:
#     if letter not in dict.keys():
#         dict[letter] = 0
#     dict[letter] += 1

# print(dict)

dict = defaultdict(int)

for letter in string:
    dict[letter] += 1
# defaultdict(<class 'int'>, {'s': 7, 'o': 8, 'm': 3, 'e': 5, ' ': 13, 't': 6, 'x': 1, 'i': 2, 'l': 2, 'g': 2, ',': 2, 'h': 2, 'r': 3, 'b': 1, 'u': 1, 'n': 3, 'a': 2, 'd': 1})
print(dict)


string = "some text is log, some is short, but long and short are not some"
dict = defaultdict(list)

for letter in string:
    dict[letter].append(letter)
print(dict)

"""
defaultdict(<class 'list'>, {'s': ['s', 's', 's', 's', 's', 's', 's'], 'o': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], 'm': ['m', 'm', 'm'], 'e': ['e', 'e', 'e', 'e', 'e'], ' ': 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 't': ['t', 't', 't', 't', 't', 't'], 'x': ['x'], 'i': ['i', 'i'], 'l': ['l', 'l'], 'g': ['g', 'g'], ',': [',', ','], 'h': ['h', 'h'], 'r': ['r', 'r', 'r'], 'b': ['b'], 'u': ['u'], 'n': ['n', 'n', 'n'], 'a': ['a', 'a'], 'd': ['d']})
"""
