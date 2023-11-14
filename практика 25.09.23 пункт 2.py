import random
list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]
print('Первый список:', list1)
print('Второй список:', list2)
list3 = []
for i in range(len(list1)):
    if i % 2 == 0:
        list3.append(list1[i])
for i in range(len(list2)):
    if i % 2 != 0:
        list3.append(list2[i])
print('Третий список:', list3)
