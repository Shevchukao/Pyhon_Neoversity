x = int(input("Введите число: "))

while x > 0:  #  Заголовок цикла
    x -= 1  # Тело цикла
    if x == 13:
        break  # /throw Error/end()
else:
    print("x <= 0")
