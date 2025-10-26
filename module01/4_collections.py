# List:

lst = [1, 2, 3.5, "a", "b", True, None, ["q", 0], (9, "a")]  # list
print("list: ", lst)
lst[1] = 4  # change second element of list from 2 to 4
print("change second element of list from 2 to 4: ", lst)
lst.append(1)  # add last element = 1
print("add last element = 1: ", lst)
lst.remove(1)  # delete first char in list = 1
print("delete first char in list = 1: ", lst)
lst.remove(1)  # delete True because it's 1 for Python
print("delete True because it's 1 for Python: ", lst)
lst.remove(1)  # delete second char in list = 1
print("delete second char in list = 1: ", lst)
i = lst.pop()  # delete last element in list using .pop() = (9, "a")
print("deleted last element using .pop(): ", i)  # print deleted last element = (9, "a")
print("list after manipulations: ", lst)  # print list after manipulations
print("type list: ", type(lst))  # type list
print("first element lst[0]: ", lst[0])  # first element = 1
print("second element lst[1]: ", lst[1])  # second element = 3.5
print("last element lst[-1]: ", lst[-1])  # last element = ['q', 0]
print("penultimate element lst[-2]: ", lst[-2])  # penultimate element = None
print(
    "last element in list and first element in inner list lst[-1][0]: ", lst[-1][0]
)  # print last element in list and first element in inner list = "q"
print(
    "last element in list and second element in inner list lst[-1][1]: ", lst[-1][1]
)  # print last element in list and second element in inner list = 0


#  True   False
#   100     0
#   "as"    ""
#          None
#   [1, 2]  []
#   (1, 2)  ()

a = len(lst)  # lenght of list lst
print("lenght of list: ", a)  # print lenght of list = six element
print(
    "last element in list len(lst) - 1: ", len(lst) - 1
)  # last element in list = fifth

b = len("abcd")  # lenght of string
print('len_string len("abcd"): ', b)  # print lenght of string len("abcd")

# Tuple:

lst_1 = [1, 2, 3.5, "a", "b", True, None, ["q", 0], (9, "a")]  # list_1
print("list lst_1: ", lst_1)  # print list lst_1
tpl = (1, 2, 3.5, "a", "b", True, None, ["q", 0], (9, "a"))  # tuple
# tpl[3] = 0 # tuple not support item assignment
tpl_from_lst_1 = tuple(lst_1)  # tuple from list
print("tuple: ", tpl)  # print tuple
lst_from_tpl = list(tpl)  # list from tuple
tpl[-2][0] = 0  # change penultimate element from "q" to 0
print("tuple after manipulations tpl[-2][0]: ", tpl)  # print tuple after manipulations
print("type tuple: ", type(tpl))  # print type tuple
print(
    "Count of 1(True and 1) in tuple", tpl.count(1)
)  # Count of 1 in tuple: True and 1
print("tuple from list lst_1: ", tpl_from_lst_1)  # print tuple from list lst
print("list from tuple tpl: ", lst_from_tpl)  # print list from tuple tpl

# Set:
lst_2 = [1, 1, 2, 3.5, "a", "b", True, None, ["q", 0], (9, "a")]
print("lst_2: ", lst_2)  # print list lst_2
tpl_2 = (1, 1, 2, 3.5, "a", "b", True, None, (9, "a"))
print("tuple tpl_2: ", tpl_2)  # print tuple tpl_2
# st = set(lst_2) # TypeError unhashable type list, not work with outer list and inner list also
st_from_tuple_without_inner_list = set(tpl_2)  # set from tuple
print(
    "set from tuple tpl_2: ", st_from_tuple_without_inner_list
)  # print set from tuple

st = {1, 2, 2, 2, 3, 5, 4, 5, 7, "a", "a"}  # set
print("set st: ", st)  # print set have only unique value, sorted with numbers
st.add(8)  # add element 8 in set st
st.add(8)  # not add because we have 8 in set
print(
    "set st with .add 8: ", st
)  # print set with add 8 with check availability element 8

# Frozenset:
fst = frozenset((1, 2, 2, 2, 3, 5, 4, 5, 7, "a", "a"))  # frozenset not changed set
# fst.add(9)  # frozenset don't have attribute .add
print("frozenset: ", fst)  # print frozenset


# Dictionary:

dct = {
    "name": "Anton",
    "age": 30,
    0: "net",
    "games": ["CSGO", "GTA5", "DOTA2"],
}  # dictionary dct
print("dictionary dct: ", dct)  # print dictionary dct
print(type(dct))
dct["mail"] = (
    "anton.shevchuk.1998@gmail.com"  # add new entry in dict.  Don't use bool key because 0 == False, 1 == True
)
print("new entry in dictionary in end: ", dct)  # print new entry in dictionary in end
dct["age"] = 27  # change old entry with key "age" = 27
print('dict with change old entry with key "age" = 30 to 27: ', dct)  # age = 30 to 27
print("keys from dictionary dct: ", dct.keys())  # keys from dictionary dct
print("values from dictionary dct: ", dct.values())  # values from dictionary dct
print("items from dictionary dct: ", dct.items())  # items from dictionary dct

a = [1, 2, 3]  # a assignment list
b = a  # b assignment link a
c = [1, 2, 3]  # c assignment list, c isn't a
d = (
    a.copy()
)  # d assignment copy list a with outer list a, not deep copy (list in list copy and change inner list in list d = change inner list in list a)
b[1] = 5  # change list b second element, also change list a second element because link
print("id a: ", id(a))  # print id a
print("id b: ", id(b))  # print id b
print("id c: ", id(c))  # print id c
print("id d: ", id(d))  # print id d
print("list a: ", a)  # print list a
print("list b: ", b)  # print list b
print("list c: ", c)  # print list c
print("list d: ", d)  # print list c
print(id(a) == id(b))
print(id(a) == id(c))
print(id(a) == id(d))
print(
    a is b
)  # True, because id(a) == id(b) checking if two variables refer to the same object, or not
print(a is c)  # False, because id(a) == id(c)
print(a is d)  # False, because id(a) == id(d)

t = ([1, 2, 3], 4, 5)  # tuple with inner list [1,2,3]
t[0][2] = 5  # can change because [1,2,3] list is link on tuple
print(t)  # print tuple
