def my_title(text):
    words, res = [], []
    if len(text) > 0:
        for i in text.split():
            words.append(i[0].upper() + i[1:])
        res = ' '.join(words)
    return res


print(my_title(input('Введите строку:')))
