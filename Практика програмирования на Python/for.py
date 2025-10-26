for x_1 in 1, 5, 2, 4, 3:  # Итерируемый обьект
    print(x_1**2)

#       => x = start
#       => while x < stop
#       =>      print(x)
#       =>      x += step

# Цикл while аналогичен чиклу ниже for(более удобен для перебора, меньше нужно строчек)

#               (  0,    end,   +1)
# for x in range(start, stop, step):  # range это функция которую мы вызываем, это генератор арифметических прогрессий
#    print(x)

A = range(1, 102, 3)  # type range
for x in A:
    print(x)

for x in range(1, 101, 1):
    print(x)

y = 1
while y < 101:
    print(y)
    y += 1
