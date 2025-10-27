
dct = {1: "Anton", 2: "Andrey", 3: "Peter", 4: "Alex"}
# [for ... in ...] construction need for iterable over a sequencence of elements(such as string, list, dictionary ,tuples, ranges)
for key in dct:
    dct[key] = dct[key]
    print(dct[key])