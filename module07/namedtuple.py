from collections import namedtuple

t1 = (2, 3)
t2 = (3, 4)
print(t1, t2)  # (2, 3) (3, 4)

h1 = ("John", "Smith", 35, "j.shith@gmail.com", +380993425055)
h2 = ("Anton", "Shevchuk", 27, "anton.shevchuk.1998@gmail.com", +380993425055)
print(
    h1, h2
)  # ('John', 'Smith', 35, 'j.shith@gmail.com', 380993425055) ('Anton', 'Shevchuk', 27, 'anton.shevchuk.1998@gmail.com', 380993425055)

Human = namedtuple("Human", ["name", "lname", "age", "email", "phone"])
h1 = Human("John", "Smith", 35, "j.shith@gmail.com", 380993425055)
# Human(name='John', lname='Smith', age=35, email='j.shith@gmail.com', phone=380993425055)
print(h1)
# There is a guy named John Smith who is age of 35, and his contacts are: email: j.shith@gmail.com, phone number: 380993425055
print(
    f"There is a guy named {h1.name} {h1.lname} who is age of {h1.age}, and his contacts are: email: {h1.email}, phone number: {h1.phone}"
)

Dot = namedtuple("Dotxy", ["x", "y"])
print(Dot)  # <class '__main__.Dotxy'>
p1 = Dot(2, 3)
p2 = Dot(y=3, x=2)
# p3 = Dot() # Error because need two argument
print(p1)  # Dotxy(x=2, y=3)
print(p2)  # Dotxy(x=2, y=3)
# print(p3)  # TypeError: Dotxy.__new__() required positional arguments: 'x' and 'y'
print(isinstance(p1, Dot), isinstance(p2, Dot))  # True, p1,p2 - object into class
# Error:
# p1.x = 3 # elment of tuple we can't change
print(f"p1.x = {p1.x}, p1.y = {p1.y}")  # p2.x = 2, p2.y = 3
print(f"p2.x = {p2.x}, p2.y = {p2.y}")  # p2.x = 2, p2.y = 3
