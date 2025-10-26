# Берем переменную i и запихиваем значения от 0 до 9, потом эту переменную запихиваем в вывод выводится в столбец по очереди
# for element in sequence

for i in range(10):
    print(i)


# Берем переменную i и запихиваем значения от 0 до 9, выводим значения через пробел в строку с помощью параметра end = " "
for i in range(10):
    print(i, end=" ")
    if i == 9:
        print("")

# print("\nEnd")

# Берем переменную name и запихиваем в нее по очереди элементы списка students с индексами сначала 0 потом 1 и т.д.
students = ["Anton", "Vasya"]

for name in students:
    print(name)

# Берем переменную letter и запихиваем в нее поочередно каждый символ с текстовой переменной
for letter in "Anton Shevchuk":
    print(letter)

""" Берем переменную x запихиваем в нее числа из диапазона (start = 1), (stop = 10 - 1), (step = 1) 
и потом при выводе в консоль попадает число в степени 2"""
for x in range(1, 10, 1):
    print(x**2)

""" Берем текст полученный от пользователя, записываем а переменную text.
Потом создаем две переменные-счетчики space_count и total_count_without_space."""
text = input("Enter the string: ")
space_count = 0
total_count_without_space = 0

""" Поочередно подсчитываем каждый символ из текстовой переменной с помощью переменной счетчика.
Проверяем далее каждый символ если " " то увеличиваем счетчик, если пробела нет увеличиваем другой счетчик.
По итогу получаем две переменные с нужным количеством знаков в словах и пробелов.
Далее сумируем две переменные для опредиления общего количества знаков в строке."""
for letter_text in text:
    if letter_text == " ":
        space_count += 1
    else:
        total_count_without_space += 1
total_count = total_count_without_space + space_count
print(
    f"Количество символов без пробелов: {total_count_without_space}, количество пробелов: {space_count}, общее количество символов в строке {total_count}"
)

name_animal = ["Teddy", "Scoof", "Garfield"]

animal = ["dog", "pig", "cat"]

for xnumber in enumerate(name_animal, start=1):
    print(xnumber)

for x_animal in zip(animal, name_animal):
    print(x_animal)

dict_animal = {"dog": "Teddy", "pig": "Scoof", "cat": "Garfield"}

for dict_animal_x in dict_animal:
    print(dict_animal_x)

for dict_animal_key in dict_animal.keys():
    print(dict_animal_key)

for dict_animal_value in dict_animal.values():
    print(dict_animal_value)

for dict_animal_item in dict_animal.items():
    print(dict_animal_item)


numbers = [1, 2, 47, 89, 14, -2, -25, 87, 65]

# Sorting min and max numbers in list
# numbers.sort()

# min_number1 = numbers[0]

# numbers.sort(reverse=True)

# max_number1 = numbers[0]

# print(f"Min number in list: {min_number1}, max number in list: {max_number1}")

# Cycle min and max numbers in list
max_number2 = numbers[0]
min_number2 = numbers[0]

for number in numbers:
    if number > max_number2:
        max_number2 = number

for number in numbers:
    if number < min_number2:
        min_number2 = number

print(f"Maximum number is: {max_number2}, minimum number is: {min_number2}")

print(f"Maximum number is: {max(numbers)}, minimum number is: {min(numbers)}")
