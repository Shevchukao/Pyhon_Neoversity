# dct = {1: "Anton", 2: "Andrey", 3: "Peter", 4: "Alex"}
# [for ... in ...] construction need for iterable over a sequencence of elements(such as string, list, dictionary ,tuples, ranges)
# for key in dct:
#     key = key * 2  # multiply keys on 2
#     print(key)  # iterable by keys
# print(dct)  # doesn't change elements in dictionary

# for key in dct:
#     dct[key] = dct[key] * 2  # multiply values on 2
#     print(dct[key])  # iterable by values
# print(dct)  # change elements in dictionary

dct1 = {1: 10, 2: 27, 5: 30}
for key, value in dct1.items():
    print(dct1[key])
    print(value)
    value *= 2  # doesn't change elements in dictionary but change elements in output
    print("Dictionary after value *= 2: ", dct1)
    dct1[key] *= 2  # change elements in dictionary and change elements in output
    print("Dictionary after dct1[key] *= 2: ", dct1)
print(dct1)
