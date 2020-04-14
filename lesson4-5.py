from functools import reduce


def multip_list(el_1, el_2):
    return el_1 * el_2


new_list = [el for el in range(100, 1001, 2)]
print(
    f'Список четных значений от 1000 до 1000\n{new_list}\nПроизведение всех элементов\n{reduce(multip_list, new_list)}')
