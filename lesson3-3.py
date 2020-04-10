def my_func(a_1, a_2, a_3):
    return sum(sorted([a_1, a_2, a_3])[1:])


print(my_func(int(input("Первый аргумент - ")), int(input("Второй аргумент -")), int(input("Третий аргумент -"))))
