import random

my_list = [random.randint(-15, 15) for i in range(25)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список\n{my_list}\nСписок уникальных элементов\n{new_list}')
