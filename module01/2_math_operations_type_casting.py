a = 5
b = 3.4

# Arithmetic operators:

print(a + b)  # sum/add addition
print(type(a + b))  # int + int = int

print(a - b)  # substraction
print(type(a - b))  # int - int = int

print(a * b)  # multiplication
print(type(a * b))  # int * int = int

print(a / b)  # division
print(type(a / b))  # int / int = float float / int = float int / float = float

print(a // b)  # floor division
print(type(a // b))  # int // int = int float // int = float int // float = float

print(a % b)  # modulo
print(type(a % b))  # int % int = int float / int = float int / float = float

print(a**b)  # exponentiation
print(type(a**b))  # int ** int = int float ** int = float int ** float = float

# Assignment operators:

c = 2  # assigning a value for variable
d = 2
e = 2
f = 2
g = 2
h = 2
k = 2
l = 2
y = 2

c = 2  # assigning a value
z = 2  # assigning a value
d += 2  # adding and assigning
e -= 2  # substracting and assigning
f *= 2  # multiplying and assigning
g /= 2  # deviding and assigning
h //= 2  # floor divisioning and assigning
k %= 2  # moduling and assigning
l **= 2  # exponentiating and assigning
z *= 5 + 6  # first 5 + 6 = 11; second 2 * 11 = 22
y **= 0.5  # or y **= .5
print(c, d, e, f, g, h, k, l, z, y)

# Comparison Operators:

m = 1
n = 2
m == n  # equal to
m != n  # not equal to
m < n  # less than
m > n  # greater than
m <= n  # less or equal than
m >= n  # less or equal than


# Logical Operators:

o = 0
p = 1

# o = 0 and p = 1  # Logical Operators AND
# o = 0 or p = 1  # Logical Operators OR
# not o = 0  # Logical Operators NOT

# Bitwise Operators:

# (&, |, ^, ~, <<, >>) (bitwise AND, OR, XOR, NOT, left shift, right shift)

# Membership Operators:
# in, not in (checking for presence in a sequence, checking for no presence in a sequence)

# Identity Operators:
# is, is not (checking if two variables refer to the same object, or not)


s1 = "Hello "
s2 = "world"
s = s1 + s2
print(s)

t1 = "2"
t2 = "3"
t = t1 + t2
print(t)

s1 = "Hello "
s2 = "world"
s3 = s1 * 3 + s2
print(s3)

t1 = "2"
t2 = int("3")
t = int(t1) + t2
print(t)
print(type(t))
t = str(t)
print(t)
print(type(t))

u1 = "2"
u2 = float("3")
u = float(u1) + u2
print(u)
print(type(u))

v1 = "2"
v2 = float("3")
v = str(float(v1) * 3) + str(v2)
print(v)
print(type(v))
