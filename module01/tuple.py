# Counting occurrences of an element in a tuple
a = ("apple", "banana", "cherry", "apple")

# Count how many times "apple" appears in the tuple
count_apple = a.count("apple")
print(count_apple)  # Output: 2

# Finding the index of an element in a tuple
b = (10, 20, 30, 20, 40)

# Find the index of the first occurrence of 40
index_20 = b.index(40)
print(index_20)  # Output: 1

# Convert tuple to list
c = list(b)
print(c)  # Output: [10, 20, 30, 20, 40]

# Convert list back to tuple
d = tuple(c)
print(d)  # Output: (10, 20, 30, 20, 40)
