with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        sal.append(i[1])
        if float(i[1]) < 20000:
            poor.append(i[0])

print(f'Оклад меньше 20000 {poor}\nCредний оклад {sum(map(float, sal)) / len(sal)}')
