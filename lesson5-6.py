x = open("text_6.txt", "r", encoding="utf-8")
y = dict()

for i in x:
    sum_number = 0
    for el in i.partition(":")[2].split():
        if el == "-":
            continue
        else:
            sum_number += int(el.partition("(")[0])
    y[i.partition(":")[0]] = sum_number
x.close()
print(y)

