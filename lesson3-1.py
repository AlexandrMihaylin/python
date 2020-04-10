def div(d_1, d_2):
    try:
        d_1, d_2 = int(d_1), int(d_2)
        divide = d_1 / d_2
    except ZeroDivisionError:
        return "Division by zero forbidden!"
    except ValueError:
        return "Value Error!"
    return round(divide, 2)


print(div(input("Делимое -"), input("Делитель - ")))
