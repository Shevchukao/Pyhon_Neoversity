dct = {1: "Anton", 2: "Andrey", 3: "Peter", 4: "Alex"}
# [for ... in ...] construction need for iterable over a sequencence of elements(such as string, list, dictionary ,tuples, ranges)
# for key in dct:
#     key = key * 2  # multiply keys on 2
#     print(key)  # iterable by keys
# print(dct)  # doesn't change elements in dictionary

# for key in dct:
#     dct[key] = dct[key] * 2  # multiply values on 2
#     print(dct[key])  # iterable by values
# print(dct)  # change elements in dictionary

# for keys in dct.keys():
#     print(keys)  # print keys dictionary dct on each itteration
# print(dct)

# for values in dct.values():
#     print(values)  # print values dictionary dct on each itteration
# print(dct)

# for values in dct.items():
#     print(values)  # print items(keys+values) dictionary dct on each itteration
# print(dct)


# count = 0 # for count cicles in output
# dct1 = {1: 10, 2: 27, 5: 30}
# for key, value in dct1.items():
#     count += 1
#     print(count, "value: ", value)  # print values without change
#     print(count, "dct1[key]: ", dct1[key])  # print values with change
#     print(count, "dictionary, before change: ", dct1)
#     value *= 2  # doesn't change elements in dictionary but change elements in output
#     print(count, "value, after value *= 2: ", value)  # print values without change
#     print(count, "dct1[key], after value *= 2: ", dct1[key])  # print values with change
#     print(count, "dictionary after value *= 2, without change: ", dct1)
#     dct1[key] *= 2  # change elements in dictionary and change elements in output
#     print(count, "dct1[key], after dct1[key] *= 2: ", dct1[key])
#     print(count, "value,  after dct1[key] *= 2: ", value)
#     print(count, "dictionary, after dct1[key] *= 2: ", dct1)
# print("final dictionary after for-in construction: ", dct1)
