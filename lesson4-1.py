from sys import argv


def salary():
    try:
        time, stavka, bonus = map(int, argv[1:])
        print(f'Заработная плата сотрудника - {time * stavka + bonus}')
    except ValueError:
        print("Введите три числа.")


salary()
