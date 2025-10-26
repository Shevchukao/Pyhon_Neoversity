#       _____
# x -->|  f  |
#      |     |--->
# y -->|_____|

#      (x,y - формальные параметры)
# def f(x,y):  # define определить f(x,y) - функцию
#    return x + y

# print(f(1,1))  # вызов функции, возможен огромное количество раз c разными фактическими параметрами


# def f(x: int, y: int): -> int:
# def f(x: "int, >0", y: "int, >0") -> int:
# return x + y
# в Python DuckTyping(в функцию можно запихнуть параметры любых типов),
# полиморфизм(преймущество интерпритируемых языков програмирования),
# можно использовать один интерфейс для разных типов и форм данных


def say_hello():
    # тело функции
    print("Привіт, Світ!")  # Кінець функції say_hello()


# вызов функции
say_hello()

# вызов функции
say_hello()


def print_max(a, b):
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "дорівнює", b)
    else:
        print(b, "максимально")


print_max(3, 4)  # прямая передача значений

x = 5
y = 7
print_max(x, y)  # передача значений в качестве аргументов функции


def print_max(a: int, b: int):  # типизация функции
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "дорівнює", b)
    else:
        print(b, "максимально")


print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів


def f(x: int, y: int) -> int:  # типизация и возврат аргументов
    return x + y


print(f(1, f(1, 2)))  # вложенные функции с фактическими параметрами
#          ---3---
#     ------4------

print(f(1.9, f(1.5, 2.3)))  # вложенные функции с фактическими параметрами
#             ---3.8---
#     --------5.7--------

print(f("Anton ", f("Hello", " World")))  # вложенные функции с фактическими параметрами
#                 -----Hello World-----
#     ---------Anton Hello World--------


def greet(name: str) -> str:  # выводит строку
    return f"Привет, {name}!"


def is_even(num: int) -> bool:  # выводит bool(False or True)
    return num % 2 == 0


def modify_string(original: str) -> str:
    original = "change"
    return original


str_var = "original"
print(modify_string(str_var))  # change
print(str_var)  # original


def modify_list(lst: list) -> None:
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # выведет [1, 2, 3, 4]


def modify_list(lst: list) -> None:
    lst = lst.copy()
    lst.append(4)


my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # виведе: [1, 2, 3]


check_even = is_even(4)
print(check_even)


greeting = greet("Антон")
print(greeting)  # Привет, Антон!


def p3(x):  # функция печати числа x три раза
    print(x)
    print(x)
    print(x)
    return


print(p3(3))  # вызов функции печати числа 3 три раза
print(p3("Hello"))  # вызов функции печати слова Hello три раза
# тип NoneType все равно что return None


def add(x, y):  # название фунции должно быть читаемым
    "Складывает x и y"  # документ строка
    return x + y


def multy_print(x):  # тут хорошее название
    print(x)
    return


print(multy_print(1))


x = 50


def func() -> None:
    x = 2
    print("Зміна локального x на", x)  # тут будет x = 2


func()
print("Глобальний x як і раніше", x)  # тут будет x = 50


def outer_func():
    enclosing_var = "Я змінна в функції, що охоплює"

    def inner_func():
        print("Всередині вкладеної функції:", enclosing_var)

    inner_func()


outer_func()


def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x


result = func_outer()


x = 50


def func():
    global x
    print("x дорівнює", x)  # x дорівнює 50
    x = 2
    print("Змінюємо глобальне значення x на", x)  # Змінюємо глобальне значення x на 2


func()
print("Значення x складає", x)  # Значення x складає 2


def greet(name, message="Привіт"):
    print(f"{message}, {name}!")


greet("Anton")  # Привіт, Anton!

greet(message="Hi", name="Anton")


def func(a, b=5, c=10):
    print("a дорівнює", a, ", b дорівнює", b, ", а c дорівнює", c)


# a дорівнює 3, b дорівнює 7, а c дорівнює 10
func(3, 7)

# a дорівнює 25, b дорівнює 5, а c дорівнює 24
func(25, c=24)

# a дорівнює 100, b дорівнює 5, а c дорівнює 50
func(c=50, a=100)


def say(message, times=1):
    print(message * times)


say("Привіт")
say("Світ", 5)


def real_cost(base: int, discount: float = 0) -> float:
    return base * (1 - discount)


price_bread = 15
price_butter = 50
price_sugar = 60

current_price_bread = real_cost(price_bread)
current_price_butter = real_cost(price_butter, 0.05)
current_price_sugar = real_cost(price_sugar, 0.07)

print(f"Нова вартість хліба: {current_price_bread}")
print(f"Нова вартість масла: {current_price_butter}")
print(f"Нова вартість цукру: {current_price_sugar}")
