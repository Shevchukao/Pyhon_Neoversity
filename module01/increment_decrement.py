# Incrementing Values
a = 0
a += 1  # Equivalent to a = a + 1
a = a + 1  # Another way to increment
print(a)  # Output: 2

# Decrementing Values
a = 0
a -= 1  # Equivalent to a = a - 1
a = a - 1  # Another way to decrement
print(a)  # Output: 1

# Multiplying Values
a = 2
a *= 2  # Equivalent to a = a * 2
a = a * 2  # Another way to multiply
print(a)  # Output: 8

# Dividing Values
a = 4
a /= 1  # Equivalent to a = a / 1
a = a / 1  # Another way to divide
print(a)  # Output: 0.0

# Modulus Operation
a = 5
a %= 2  # Equivalent to a = a % 2
a = a % 2  # Another way to get the remainder
print(a)  # Output: 1

# Exponentiation
a = 3
a **= 2  # Equivalent to a = a ** 2
a = a**2  # Another way to exponentiate
print(a)  # Output: 81

# Floor Division
a = 5
a //= 2  # Equivalent to a = a // 2
a = a // 2  # Another way to perform floor division
print(a)  # Output: 1

# Combining Multiple Operations
a = 2
a += 3  # a = 5
a *= 2  # a = 10
a -= 4  # a = 6
a /= 2  # a = 3.0
print(a)  # Output: 3.0

# Using Parentheses for Clarity
a = 2
a = (a + 3) * 2 - 4 / 2  # Equivalent to a = ((a + 3) * 2) - (4 / 2)
print(a)  # Output: 8.0

# Using Increment and Decrement in Loops
a = 0
for i in range(5):
    a += 1  # Incrementing in each iteration
print(a)  # Output: 5

b = 10
for i in range(5):
    b -= 2  # Decrementing in each iteration
print(b)  # Output: 0
