#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b
# и  выводить одно натуральное число — номер дня. Например: a = 2, b = 3.

a = int(input('Введите а - '))
b = int(input('Введите b - '))
day = 1
while a < b:
    a *= 1.1
    day += 1
print('На достижение таких результатов понадобится {} дней.'.format(day))
