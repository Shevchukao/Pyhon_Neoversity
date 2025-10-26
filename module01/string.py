# This is a string variable
string = "Anton"
print(string)

# This is also a string variable
string = "Anton"
print(string)

# This is a string variable using triple quotes
string = """Anton"""
print(string)

# Single line string
name = "Welcome to Anton's website, please choose the option: 1-> enter map, 2-> exit"
print(name)

# Using backslash for line continuation
name = "Welcome to Anton's website, please choose the option: \
1-> enter map \
2-> exit"
print(name)

# Using newline characters
name = (
    "Welcome to Anton's website, please choose the option: \n1-> enter map \n2-> exit"
)
print(name)

# Using triple quotes for multi-line string
name = """Welcome to Anton's website, please choose the option:
1-> enter map
2-> exit"""
print(name)

# Using multiple print statements
print("Welcome to Anton's website, please choose the option:")
print("1-> enter map")
print("2-> exit")

# String concatenation and repetition
name = "A" + "A"  # Concatenation
print(name * 10)  # Repetition
