# Demonstrating various list1 methods in Python
list1 = []

# Extending the list1 with elements 1, 2, 3
list1.extend([1, 2, 3])
print(list1)  # [1, 2, 3]

# Appending element 4 to the end of the list1
list1.append(4)
print(list1)  # [1, 2, 3, 4]

# Inserting element 10 at index 2
list1.insert(2, 10)
print(list1)  # [1, 2, 10, 3, 4

# Removing element 10
list1.remove(10)
print(list1)  # [1, 2, 3, 4]

# Trying to remove an element not in the list1
# list1 remove(5)  # ValueError: list1.remove(x): x not in list1
# print(list1)

# Popping last element
list1.pop()
print(list1)  # [1, 2, 3]

# Popping element at index 2
list1.pop(2)
print(list1)  # [1, 2]

# Trying to pop from an invalid index
# list1.pop(3)
# print(list1)  # IndexError: pop index out of range

# Clearing the list1
list1.clear()
print(list1)  # []

list1.extend([1, 2, 3])
print(list1)  # [1, 2, 3]

# Copying the list1
new_list1 = list1.copy()
print(new_list1)  # [1, 2, 3]

# Reversing the list1
list1.reverse()
print(list1)  # [3, 2, 1]

# Sorting the list1
list1.sort()
print(list1)  # [1, 2, 3]

# Counting occurrences of element 2
print(list1.count(2))  # 1

# Finding index of element 2
print(list1.index(2))  # 1

# Deleting element at index 1
del list1[1]
print(list1)  # [1, 3]

# Trying to delete an element at an invalid index
# del list1[5]
# print(list1)  # IndexError: list1 assignment index out of range

# Concatenating list1s using +
list11 = [1, 2]
list12 = [3, 4]
combined_list1 = list11 + list12
print(combined_list1)  # [1, 2, 3, 4]

# Repeating list1s using *
repeated_list1 = list11 * 3
print(repeated_list1)  # [1, 2, 1, 2, 1, 2]

# Iterating through the list1
for item in list11:
    print(item)  # 1

word = "Hello"
list_from_word = list(word)
print(list_from_word)  # ['H', 'e', 'l', 'l', 'o']
