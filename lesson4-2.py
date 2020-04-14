import random

my_list = [el * random.randint(0, 100) for el in range(0, 10)]
print(f'Исходный список - {my_list}')
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(f'Новый список - {new_list}')
