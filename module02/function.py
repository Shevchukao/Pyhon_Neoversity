def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old.")


print(greet("Anton", 27))


def add(x, y):
    return x + y


print(add(4, 5))

multiply = lambda x, y: x * y
print(multiply(10, 20))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def even_numbers(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum


x = [1, 2, 3, 4, 5]
print(even_numbers(x))


def vowels_letters(text):
    count_letters = 0
    for letter in text.lower():
        if letter in "aeiou":
            count_letters += 1
    return count_letters


text = input("Enter some words: ")
print(vowels_letters(text))

# def factorial_1(n):
#     result = 1
#     for x in range(1, n+1):
#         result *= x
#     return result

# print(factorial_1(5))


# def factorial_1(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_1(n-1)


# print(factorial_1(5))

# help(str)


def reverse_string(text_1):
    return text_1[::-1]


print(reverse_string("Anton"))


def count_words(textx):
    return len(textx.split())


textx = "Hello World"
print(count_words(textx))
