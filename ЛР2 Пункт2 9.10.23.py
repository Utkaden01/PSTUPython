class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'Стек пуст.'
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Стек пуст.'
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print('Стек пуст.')
        else:
            print('Стек сейчас:')
            for item in reversed(self.stack):
                print(item)


stack = Stack()

while True:
    print('Меню:')
    print('1. Добавить элемент в стек')
    print('2. Удалить элемент из стека')
    print('3. Верхний элемент стека')
    print('4. Отобразить стек')
    print('5. Выйти')

    choice = input('Ваш выбор: ')

    if choice == '1':
        item = input('Введите элемент: ')
        stack.push(item)
        print('Элемент успешно добавлен в стек.')
    elif choice == '2':
        popped_item = stack.pop()
        print('Удаленный элемент из стека:', popped_item)
    elif choice == '3':
        top_item = stack.peek()
        print('Верхний элемент стека:', top_item)
    elif choice == '4':
        stack.display()
    elif choice == '5':
        print('Программа завершена.')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')
