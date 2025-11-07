from collections import namedtuple

t1 = (2, 3)
t2 = (3, 4)
print(t1, t2)  # (2, 3) (3, 4)

h1 = ("John", "Smith", 35, "j.shith@gmail.com", +380993425055)
h2 = ("Anton", "Shevchuk", 27, "anton.shevchuk.1998@gmail.com", +380993425055)
print(
    h1, h2
)  # ('John', 'Smith', 35, 'j.shith@gmail.com', 380993425055) ('Anton', 'Shevchuk', 27, 'anton.shevchuk.1998@gmail.com', 380993425055)

Dot = namedtuple("Dotxy", ["x", "y"])
print(Dot)  # <class '__main__.Dotxy'>
p1 = Dot(2, 3)
p2 = Dot(y=3, x=2)
print(p1)  # Dotxy(x=2, y=3)
print(p2)  # Dotxy(x=2, y=3)
# Error:
# p1.x = 3 # elment of tuple we can't change
print(f"p1.x = {p1.x}, p1.y = {p1.y}")  # p2.x = 2, p2.y = 3
print(f"p2.x = {p2.x}, p2.y = {p2.y}")  # p2.x = 2, p2.y = 3
