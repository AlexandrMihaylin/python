def my_sum():
    x = False
    fSum = 0
    while x == False:
        numb = input("Введите строку чисел, раздеоленных пробелами, используйте n для выхода - ").split()
        res = 0
        for i in range(len(numb)):
            if numb[i] == 'n':
                x = True
                break
            else:
                res = res + int(numb[i])
        fSum = fSum + res
        print(f"Текущая сумма равна {fSum}")
    print(f"Окончательная сумма равна {fSum}")


my_sum()
