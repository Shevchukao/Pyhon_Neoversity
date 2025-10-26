# Теория: Методы для работы со списками в Python

# 1. append(x)
# Добавляет элемент x в конец списка.
list = [1, 2, 3]
list.append(4)
print(list)  # [1, 2, 3, 4]

# 2. extend(iterable)
# Расширяет список, добавляя все элементы из iterable.
list.extend([5, 6])
print(list)  # [1, 2, 3, 4, 5, 6]

# 3. insert(i, x)
# Вставляет элемент x на индекс i.
list.insert(2, 10)
print(list)  # [1, 2, 10, 3, 4, 5, 6]

# 4. remove(x)
# Удаляет первый элемент, равный x.
list.remove(10)
print(list)  # [1, 2, 3, 4, 5, 6]

# 5. pop([i])
# Удаляет и возвращает элемент по индексу i. Если индекс не указан, удаляет последний элемент.
list.pop()
print(list)  # [1, 2, 3, 4, 5]

# 6. clear()
# Удаляет все элементы из списка.
list.clear()
print(list)  # []

# 7. copy()
# Создает поверхностную копию списка.
list = [1, 2, 3]
new_list = list.copy()
print(new_list)  # [1, 2, 3]

# 8. reverse()
# Переворачивает список на месте.
list.reverse()
print(list)  # [3, 2, 1]

# 9. sort()
# Сортирует список на месте по возрастанию.
list.sort()
print(list)  # [1, 2, 3]

# 10. count(x)
# Возвращает количество элементов x в списке.
print(list.count(2))  # 1

# 11. index(x)
# Возвращает индекс первого вхождения элемента x в список.
print(list.index(2))  # 1

# 12. del
# Оператор для удаления элемента по индексу или среза.
del list[1]
print(list)  # [1, 3]

# 13. Срезы
# Извлечение подсписка.
sublist = list[1:]
print(sublist)  # [3]

# 14. Конкатенация ( + )
# Соединяет два списка.
list2 = [4, 5, 6]
combined = list + list2
print(combined)  # [1, 3, 4, 5, 6]

# 15. Умножение списка ( * )
# Повторяет список.
multiplied = list * 3
print(multiplied)  # [1, 3, 1, 3, 1, 3]

# 16. all() и any()
# all() проверяет, что все элементы истинны, any() - что хотя бы один.
print(all([True, True, False]))  # False
print(any([True, False, False]))  # True

# 17. map()
# Применяет функцию ко всем элементам списка.
squared = list(map(lambda x: x**2, list))
print(squared)  # [1, 9]

# 18. filter()
# Отфильтровывает элементы списка.
even_list = list(filter(lambda x: x % 2 == 0, list))
print(even_list)  # [2]

# 19. zip()
# Объединяет несколько списков.
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]
