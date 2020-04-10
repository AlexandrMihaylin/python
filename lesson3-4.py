# вариант с **

def my_func(x, y):
    try:
        res_pow = x ** y
    except TypeError:
        return "Введите рациональное число и отрицательную степень"
    return round(res_pow, 4)


print(my_func(float(input("Рациональное число - ")), float(input("Отрицательная степень - "))))

#вариант с циклом

def my_pow(x, y):
    try:
        x, y = float(x), int(y)
        res = x
        for _ in range(abs(y)-1):
            res *= x
        return f"{1/res:.4f}"
    except ValueError:
        return "Value Error"


print(my_pow(input("Рациональное число - "), input("Отрицательная степень -")))