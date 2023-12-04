import json

# Функция для загрузки данных из JSON-файла


def load_data():
    try:
        with open('budget_tracker.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

# Функция для сохранения данных в JSON-файл


def save_data(data):
    with open('budget_tracker.json', 'w') as file:
        json.dump(data, file)

# Функция для добавления операции


def add_operation(data):
    description = input("Введите описание операции: ")
    amount = float(input("Введите сумму операции: "))
    category = input("Введите категорию операции: ")

    # Проверка, существует ли уже категория в данных
    if category in data:
        data[category].append({"description": description, "amount": amount})
    else:
        data[category] = [{"description": description, "amount": amount}]

    save_data(data)
    print("Операция успешно добавлена!")

# Функция для вывода списка операций


def show_operations(data):
    category = input(
        "Введите категорию для просмотра операций (или оставьте пустым для просмотра всех): ")

    if category == "":
        for category in data:
            print(f"Категория: {category}")
            for operation in data[category]:
                print(
                    f"Описание: {operation['description']}, Сумма: {operation['amount']}")
    else:
        if category in data:
            print(f"Категория: {category}")
            for operation in data[category]:
                print(
                    f"Описание: {operation['description']}, Сумма: {operation['amount']}")
        else:
            print("Категория не найдена!")

# Функция для аналитики трат/доходов по категориям


def analyze_category(data):
    category = input(
        "Введите категорию для аналитики (или оставьте пустым для анализа всех): ")

    if category == "":
        for category in data:
            total_amount = sum([operation["amount"]
                               for operation in data[category]])
            print(f"Категория: {category}, Общая сумма: {total_amount}")
    else:
        if category in data:
            total_amount = sum([operation["amount"]
                               for operation in data[category]])
            print(f"Категория: {category}, Общая сумма: {total_amount}")
        else:
            print("Категория не найдена!")

# Функция для установки лимита на категорию


def set_limit(data):
    category = input("Введите категорию для установки лимита: ")
    limit = float(input("Введите лимит: "))

    if category in data:
        data[category]["limit"] = limit
    else:
        data[category] = {"limit": limit}

    save_data(data)
    print("Лимит успешно установлен!")

# Основная функция программы


def budget_tracker():
    data = load_data()

    while True:
        print("1. Добавить операцию")
        print("2. Показать список операций")
        print("3. Анализ трат/доходов по категориям")
        print("4. Установить лимит на категорию")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_operation(data)
        elif choice == "2":
            show_operations(data)
        elif choice == "3":
            analyze_category(data)
        elif choice == "4":
            set_limit(data)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")


budget_tracker()
