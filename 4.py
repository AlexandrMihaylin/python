# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число - '))
biggest = 0
while number != 0:
    num = number % 10
    if num > biggest:
        biggest = num
    number //= 10
print(biggest)
