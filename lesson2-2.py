#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения
# списка элементов необходимо использовать функцию input().


user_list = input("Введите элементы списка разделив их пробелами: ").split()
i= 0
print (f'Исходный список {user_list}')
while i + 1 < len(user_list):
    if i % 2 == 0:
        user_list.insert(i, user_list.pop(i + 1))
    i += 1
print(f"Измененный список {user_list}")