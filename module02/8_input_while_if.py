# n = None   # Problem with 0
# while not n:  # will be problem with 0 because not 0 and not None will be False
#     a = input(
#         "Enter your number: "
#     )  # it's string if you enter number you need use formating type
#     if a.isnumeric(): # check enter number
#         n = int(a)
# print(n)
# print(type(n))

# n = None
# while n is None:  # while n is None
#     a = input(
#         "Enter your number: "
#     )  # it's string if you enter number you need use formating type
#     if a.isnumeric():  # check enter number / type float isn't numeric
#         n = int(a)
# print(n)
# print(type(n))

a = input(
    "Enter your number: "
)  # it's string if you enter number you need use formating type
if a.isnumeric():  # check enter number
    n = int(a)
print(n)
print(type(n))
