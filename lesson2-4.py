#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку из нескольких слов, разделенных пробелами: ').split()

for i, x in enumerate(user_string, 1):
    print(f'{i} {x[:10]}')
