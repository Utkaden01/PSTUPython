import random

# Генерация первого словаря
dict1 = {str(i): random.randint(1, 10) for i in range(5)}
print("Первый словарь:", dict1)

# Генерация второго словаря
dict2 = {str(i): random.randint(1, 10) for i in range(5)}
print("Второй словарь:", dict2)

# Нахождение пересечения значений словарей
intersection = set(dict1.values()) & set(dict2.values())
print("Пересечение значений:", intersection)

# Создание пар "ключ - значение", значения которых попадают в пересечение для каждого из словарей
new_dict1 = {key: value for key,
             value in dict1.items() if value in intersection}
new_dict2 = {key: value for key,
             value in dict2.items() if value in intersection}

# Создание нового словаря, содержащего все пары "ключ - значение" из обоих словарей
new_dict1.update(new_dict2)

print("Новый словарь:", new_dict1)
