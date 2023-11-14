import random
numbers = [random.randint(1, 100) for _ in range(10)]
print('Исходный список:', numbers)
reversed_numbers = numbers[::-1]
print('Перевернутый список:', reversed_numbers)
