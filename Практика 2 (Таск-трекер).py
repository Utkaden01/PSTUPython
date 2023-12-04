import json

# Загрузка данных из файла JSON при запуске программы


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Сохранение списка задач в файл JSON


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Вывод списка задач на экран


def print_tasks(tasks):
    if not tasks:
        print('Список задач пуст')
        return

    print('Список задач:')
    for task_id, task in tasks.items():
        done_status = 'Х' if task['done'] else ' '
        print(f"- {done_status} {task['description']} {task['categories']}")

# Добавление новой задачи


def add_task(tasks):
    description = input('Введите описание задачи: ')
    categories = input('Введите категории задачи (через пробел): ').split()

    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        'description': description,
        'categories': categories,
        'done': False
    }

    print('Задача добавлена')

# Отметка задачи как выполненной


def mark_task_done(tasks):
    task_id = input(
        'Введите номер задачи, которую хотите отметить как выполненную: ')

    if task_id in tasks:
        tasks[task_id]['done'] = True
        print('Задача отмечена как выполненная')
    else:
        print('Задача не найдена')

# Поиск задачи по описанию


def search_task(tasks):
    keyword = input('Введите ключевое слово для поиска задач: ')

    found_tasks = []
    for task_id, task in tasks.items():
        if keyword in task['description']:
            found_tasks.append(task)

    if found_tasks:
        print(f"Найдены задачи по ключевому слову '{keyword}':")
        for task in found_tasks:
            print(f"- {task['description']} {task['categories']}")
    else:
        print('Задачи по заданному ключевому слову не найдены')

# Вывод задач по категории


def print_tasks_by_category(tasks):
    category = input('Введите категорию: ')

    category_tasks = []
    for task_id, task in tasks.items():
        if category in task['categories']:
            category_tasks.append(task)

    if category_tasks:
        print(f"Задачи в категории '{category}':")
        for task in category_tasks:
            done_status = 'X' if task['done'] else ' '
            print(
                f"- {done_status} {task['description']} {task['categories']}")
    else:
        print(f"Задачи в категории '{category}' не найдены")

# Основная функция программы


def main():
    # Загрузка задач из файла
    tasks = load_tasks()

    # Основной цикл программы
    while True:
        print('Меню:')
        print('1. Вывести список задач')
        print('2. Добавить новую задачу')
        print('3. Отметить задачу как выполненную')
        print('4. Поиск задачи по описанию')
        print('5. Вывод задач по категории')
        print('6. Выйти')

        choice = input('Введите номер пункта меню: ')

        if choice == '1':
            print_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            search_task(tasks)
        elif choice == '5':
            print_tasks_by_category(tasks)
        elif choice == '6':
            # Сохранение задач в файл перед выходом
            save_tasks(tasks)
            print('Задачи сохранены в файл')
            break
        else:
            print('Неверный выбор. Попробуйте снова.')


# Запуск программы
if __name__ == '__main__':
    main()
