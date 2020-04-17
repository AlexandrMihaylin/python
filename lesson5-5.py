from random import randint

my_list = [randint(-10, 10) for i in range(25)]
my_str = (' '.join(map(str, my_list)))


def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            file_obj.writelines(my_str)
            my_numb = my_str.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('IOError')
    except ValueError:
        print('ValueError')


summary()
