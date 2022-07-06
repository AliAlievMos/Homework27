from collections import Counter
import numpy


# задание 1


line = [1, 1, 4, 4, 7, 12, 10]


def function1(line: list):
    counter = dict(Counter(line))
    max_repeat = 0
    max_list = []
    for i in counter:
        if counter[i] == 1:
            continue
        else:
            if counter[i] > max_repeat:
                max_list = []
                max_repeat = counter[i]
                max_list.append(i)
            if counter[i] == max_repeat:
                max_repeat = counter[i]
                max_list.append(i)
    max_list = set(max_list)
    print(max_list)


function1(line)

# задание 2


def function2_main():
    storage = {}
    menu = '___МЕНЮ___\n1)ввести данные\n2)вывести все введенные данные\n3)выход'
    while True:
        print(menu)
        a = input()
        if a == '1':
            function2_1(storage)
        if a == '2':
            function2_2(storage)
        if a == '3':
            print('Выхожу')
            break


def function2_1(storage: dict):
    print('Введите название товара')
    name = input()
    print('Введите колличество товара')
    qty = input()
    print('Введите стоимость товара')
    price = input()
    storage[name] = [f'колличество:{qty}', f'стоимость:{price}']


def function2_2(storage: dict):
    print('СПИСОК ТОВАРОВ')
    for key in storage:
        print(key, '->', storage[key])


function2_main()


# задание 2*


# line = list(input())
line = [0, 1, 0, 0, 0, 1, 1]


def function2x_main(line: list):
    length = 0
    maxlength = 0
    index_of_final_length = 0
    for i in range(len(line)):
        if line[i] == 0:
            length += 1
            if i == len(line)-1:
                if maxlength/2 < length:
                    print(i)
                else:
                    function2x_arithmetic_mean(index_of_final_length, maxlength)
        else:
            if maxlength < length:
                maxlength = length
                index_of_final_length = i
                length = 0
    function2x_arithmetic_mean(index_of_final_length, maxlength)


def function2x_arithmetic_mean(index_of_final_length: int, maxlength: int): print(int(numpy.mean([index_of_final_length - maxlength, index_of_final_length - 1])))


function2x_main(line)
