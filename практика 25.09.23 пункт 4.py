import random

# Генерация словаря


def generate_dict():
    my_dict = {}
    for _ in range(10):
        key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        value = random.uniform(1, 100)
        my_dict[key] = value
    return my_dict

# Создание списка кортежей


def create_tuples(my_dict):
    unique_values = set(my_dict.values())
    tuples_list = []
    for value in unique_values:
        keys = [key for key, val in my_dict.items() if val == value]
        tuples_list.append((value, keys))
    return tuples_list

# Вывод в консоль


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    print()


def print_tuples(tuples_list):
    for value, keys in tuples_list:
        print(f"{value}: {keys}")
    print()


random_dict = generate_dict()
print("Сгенерированный словарь:")
print_dict(random_dict)
print("Список кортежей для сгенерированного словаря:")
tuples_list = create_tuples(random_dict)
print_tuples(tuples_list)
