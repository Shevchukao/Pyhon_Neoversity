lst = [1, 3, 5, 7, 9]
for element in lst:
    print(element * element)  # 1**2, 3**2, 5**2, 7**2, 9**2

lst = [1, 3, 5, 7, 9]
for element in lst:  # for work with element such as elements in list lst
    element = (
        element * element
    )  # element squared (two square of elements list lst), don't change elements in lst
    print(element)  # 1, 9, 25, 49, 81
print(lst)  # [1,3,5,7,9]

lst = [1, 3, 5, 7, 9]
for i in range(len(lst)):  # sequence from 0 to len(lst) == 5(excluded or -1)
    lst[i] = lst[i] * lst[i]  # change elements in lst
    print(lst[i])  # [1, 9, 25, 49, 81]
print(lst)  # 1, 9, 25, 49, 81
