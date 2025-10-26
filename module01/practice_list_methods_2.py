list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_1.append(11)
print("After append:", list_1)

list_1.extend([12, 13, 14])
print("After extend:", list_1)

list_1.insert(0, 10)
print("After insert at index 0:", list_1)

list_1.remove(7)
print("After remove 7:", list_1)

popped_element = list_1.pop()
print("After pop:", list_1)

list_1.reverse()
print("After reverse:", list_1)

list_1.sort(reverse=True)
print("After sort:", list_1)

list_1.remove(10)
print("After removing first occurrence of 10:", list_1)

list_1.index(1)
print("Index of 13:", list_1.index(1))

list_1.insert(12, 0)
print("After inserting 0 at index 12:", list_1)

list_2 = list_1.copy()
print("List_2:", list_2)

list_3 = list_2[2:6]
print("Sliced list_3 (index 2 to 5):", list_3)

list_4 = list_2[3:]
print("Sliced list_4 (from index 3 to end):", list_4)

list_5 = list_2[::2]
print("Sliced list_5 (every second element):", list_5)

list_6 = list_2[::-3]
print("Sliced list_6 (every third element in reverse):", list_6)

list_7 = list_2.count(3)
print("Count of 3 in list_2:", list_7)

list_8 = len(list_2)
print("Length of list_2:", list_8)

list_9 = list_2.index(11)
print("Index of 11 in list_2:", list_9)

list_2.clear()
print("After clear, list_2:", list_2)

list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "cherry", "date", "elderberry"]
zipped_list = list(zip(list1, list2))
print("Zipped list:", zipped_list)

list_unzipped = list(zip(*zipped_list))
print("Unzipped lists:", list_unzipped)

list_x = [x for x in range(5) if x % 2 == 0]
print("List comprehension (even numbers 0-9):", list_x)

list_y = [y for y in range(10) if y > 5]
print("List comprehension (numbers greater than 5):", list_y)

del list_y[1:4]
print("After deleting indices 1 to 3 from list_y:", list_y)

list_z = [3, 3.14, "hello", True, None, [1, 2, 3], (4, 5), {"key": "value"}]
print("List with mixed data types:", list_z)

