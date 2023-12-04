class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return 'Очередь пуста.'
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return 'Очередь пуста.'
        return self.queue[0]

    def display(self):
        if self.is_empty():
            print('Очередь пуста.')
        else:
            print('Очередь сейчас:')
            for item in self.queue:
                print(item)


queue = Queue()

while True:
    print('Меню:')
    print('1. Добавить элемент в очередь')
    print('2. Удалить элемент из очереди')
    print('3. Верхний элемент очереди')
    print('4. Отобразить очередь целиком')
    print('5. Выйти')

    choice = input('Ваш выбор: ')

    if choice == '1':
        item = input('Введите элемент: ')
        queue.enqueue(item)
        print('Элемент успешно добавлен в очередь.')
    elif choice == '2':
        dequeued_item = queue.dequeue()
        print('Удаленный элемент из очереди:', dequeued_item)
    elif choice == '3':
        top_item = queue.peek()
        print('Верхний элемент очереди:', top_item)
    elif choice == '4':
        queue.display()
    elif choice == '5':
        print('Программа завершена.')
        break
    else:
        print('Неверный выбор. Пожалуйста, выберите снова.')
