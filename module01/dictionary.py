# Example of a dictionary in Python
cars = {2000: "Toyota", 2005: "Honda", 2010: "Ford"}
print(cars[2005])

# Example of a dictionary with list values
year_birthday = {
    1998: ["Anton Shevchuk", "Andriy Shevchenko"],
    2004: ["Andriy Shevchenko", "Serhiy Rebrov"],
}
print(year_birthday[1998])

year_birthday_1 = {
    1998: ["Anton Shevchuk", "Andriy Shevchenko"],
    1999: ["Andriy Shevchenko", "Serhiy Rebrov"],
}
print(year_birthday_1[1998])

# Accessing the keys of the dictionary
year_birthday_1.keys()
print(year_birthday_1.keys())

# Accessing the values of the dictionary
year_birthday_1.values()
print(year_birthday_1.values())

# Accessing the items of the dictionary
year_birthday_1.items()
print(year_birthday_1.items())

# Adding a new key-value pair to the dictionary
year_birthday_1[2000] = ["Vasyl Lomachenko", "Oleksandr Usyk"]
print(year_birthday_1)

year_birthday_1.update({2001: ["Lionel Messi", "Cristiano Ronaldo"]})
print(year_birthday_1)

# Removing a key-value pair from the dictionary
del year_birthday_1[1999]
print(year_birthday_1)

# Using pop() to remove a key-value pair
year_birthday_1.pop(2001)
print(year_birthday_1)

# Using popitem() to remove the last inserted key-value pair
year_birthday_1.popitem()
print(year_birthday_1)

# Clearing the dictionary
# year_birthday_1.clear()

year_birthday_1.copy()
print(year_birthday_1)

year_birthday_1.get(1998)
print(year_birthday_1.get(1998))
