str = "Hello world"
print(
    "slice string from 2 to 6 elements str[2:7]: ", str[2:7]
)  # slice 2 to 6 start = 2 to end - 1 = 7 - 1 = 6 -> "llo w"

#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] indexes of list lst
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # list lst
print("list lst: ", lst)  # print list lst
print(
    "slice list from 1 to 2 lst[1:3]: ", lst[1:3]
)  # slice string from 1 to 2 (start(inclused) def = 0, end(excluded) or end - 1, step) start = 1 to end - 1 = 3 - 1 = 2  -> [2, 3]
print(
    "slice list from 1 to 7 lst[1:7]: ", lst[1:7]
)  # slice string from 1 to 7 start = 1 to end - 1 = 7 - 1 = 6  -> [2, 3, 4, 5, 6, 7]
print(
    "slice list all elements lst[:]: ", lst[:]
)  # slice list all elements -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(
    "slice list from 5 to end list lst[5:]: ", lst[5:]
)  # slice list from 5 to end list -> [6, 7, 8, 9, 0]
print(
    "slice list from 0 to 5 - 1 = 4 lst[:5]: ", lst[:5]
)  # slice list from 0 to 5 - 1 = 4 -> [1, 2, 3, 4, 5]
print(
    "slice list from 1 to 8 - 1 = 7 with step 2 lst[1:8:2]: ", lst[1:8:2]
)  # slice list from 1 to 8 - 1 = 7 with step 2 -> [2, 4, 6, 8]
print(
    "slice list from 1 to 8 - 1 = 7 with step 3 lst[1:8:3]: ", lst[1:8:3]
)  # slice list from 1 to 8 - 1 = 7 with step 3 -> [2, 5, 8]

#      [-10 -9 -8, -7, -6, -5, -4, -3, -2, -1] minus indexes of list lst
#       [0,  1, 2,  3,  4,  5,  6,  7,  8,  9] indexes of list lst
# lst = [1,  2, 3,  4,  5,  6,  7,  8,  9,  0]  # list lst
print(
    "slice list from 4 to -2 lst[4:-2]: ", lst[4:-2]
)  # slice list from 4 to -2 -> [5, 6, 7, 8]
print(
    "slice list from -2 to 1 with default step = 1 lst[-2:1]: ", lst[-2:1]
)  # slice list from -2 to 1 with default step = 1-> []
print(
    "slice list from -2 to 1 with step -1 lst[-2:1:-1]: ", lst[-2:1:-1]
)  # slice list from -2 to 1 with step -1 -> [9, 8, 7, 6, 5, 4, 3]
print(
    "slice reverse list with step -1 lst[::-1]: ", lst[::-1]
)  # slice reverse list with step -1 -> [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

start = -2
end = 2
step = -1

print(
    "slice reverse list from start = -2 to end = 2 with step = -1 using variable lst[-2:2:-1]: ",
    lst[-2:2:-1],
)  # slice reverse list from start = -2 to end = 2 with step = -1 using variable -> [9, 8, 7, 6, 5, 4]

list_copy = lst[::]  # copy list lst in lisp_copy
print(
    "slice for copy list lst lst[::]: ",
    lst[::],
)  # slice for copy list lst to list_copy -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_copy[5] = 10
print(
    "slice for copy list lst with change sixth element to 10 list_copy[5] = 10:",
    list_copy,
)  # slice for copy list lst with change sixth element to 10 -> [0, 1, 2, 3, 4, 5, 10, 7, 8, 9]
