import itertools

# uтератор, генерирующий целые числа, начиная с указанного, Enter - следуещее число, # - выход из программы
for el in itertools.count(int(input('Стартовое число - '))):
    print(el, end='')
    exit = input()
    if exit == '#':
        break

# итератор, повторяющий элементы некоторого списка, определенного заранее,
# Enter - следуещее число, # - выход из программы

print(
    'Повторяем элементы  списка, определенного заранее, Enter - следуещее повторение, # - выход из программы')
my_list = ["python", "java", "perl", "javascript", "C++"]
iter = itertools.cycle(my_list)
exit = None

while exit != '#':
    print(next(iter), end='')
    exit = input()
