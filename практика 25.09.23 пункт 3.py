import random
random_list = []
for _ in range(10):
    random_type = random.choice([int, float, str])
    if random_type == int:
        random_list.append(random.randint(1, 10))
    elif random_type == float:
        random_list.append(random.uniform(1.0, 10.0))
    else:
        random_list.append(random.choice(['car', 'house', 'dog', 'orange']))
print(random_list)
result_list = []
for i in range(len(random_list)):
    if str(random_list[i]) not in result_list:
        result_list.append(random_list[i])
print(result_list)
