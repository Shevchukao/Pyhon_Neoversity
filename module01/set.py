l1 = set(["Red", "Green", "Black", "White"])
l2 = set(["Red", "White", "Purple"])

# res = l1.intersection(l2)
# | = pipe
#  & - перетин, | об'єднання, ^ симетрична різниця, - різниця

# always return a copy

print(l1.union(l2))
print(l1 | l2)

print(l1.intersection(l2))
print(l1 & l2)

print(l1.difference(l2))
print(l1 - l2)

print(l1.symmetric_difference(l2))
print(l1 ^ l2)

l1.isdisjoint(l2)  # Determines whether or not two sets have any elements in common


print(l2.issubset(l1))


my_set = {4, 6, "Oleg", "Python", 100}
my_set.add("Daria")
print("Daria" in my_set)

my_set.remove("Daria")
my_set.discard("Daria")  #
# https://realpython.com/python-sets/

list1 = [1, 2, 3, 4, 55, 13, 21, 100]
list2 = [2, 2, 2, 33, 3, 3, 5, 4]

set1 = set(list1)
set2 = set(list2)
print(set1, set2)

set_union = set1 | set2
print(list(set_union))

set_cross = set1 & set2
print(list(set_cross))

list_daria = ["Red", "Green", "Black", "White"]
list_oleg = ["Red", "White", "Black", "Yellow"]

list_only_daria = list(set(list_daria) - set(list_oleg))
print(list_only_daria)


list_u = list(set(list_daria) ^ set(list_oleg))
print(list_u)
