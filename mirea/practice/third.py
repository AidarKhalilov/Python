import sys
import csv
import traceback

import matplotlib.pyplot as plt
import numpy as np
import random as rand
import math
import math
from math import pi


print(pi)
pi = 3.14
print(pi)
print(math.pi)


# Задача 1. Приведите примеры кода, которые соответствуют нарушениям PEP 8:
# 1. вызов функции foo ()
# 2. a+b
# 3. foo(a,b)
# 4. print(something, sep = ' ')
# 5. 2 строчки между определениями функций
# 6. if x > 5: y = 10
# 7. a = 5; b = 7
# 8. if something == None
# 9. if something == True


# Задача 2. Как вы думаете, модуль загружается один раз или загружается
# каждый раз при очередном импорте?
# Докажите правильность вашей гипотезы кодом.
# Модули Python не импортируются несколько раз, поэтому повторное выполнение
# команды оператора импорта не приведет к перезагрузке модуля. Если вы хотите,
# чтобы он был перезагружен, вам необходимо выполнить инструкцию reload.
# print(sys.modules)

# Задача 3. GLOBAL VARIABLE относится только к одному пользователю

# Задача 6. Напишите функцию, которая добавляет информацию о возникшем
# исключении (класс, сообщение, трассировка) в лог-файл.
def delete(z):
    try:
        math.log(z)
    except (ZeroDivisionError, ValueError) as e:
        return get_exception_info(e)


def run_with_log(func):
    with open('error_log.txt', 'w', -1, 'utf-8') as f:
        f.write(f"{str(func)} {sys.exc_info()} - your error")


def get_exception_info(func) -> str:

    exc_type, exc_value, exc_traceback = sys.exc_info()

    lines = traceback.format_exception(

        exc_type, exc_value, exc_traceback)

    log = "".join(line for line in lines)

    with open('error_log.txt', 'w', -1, 'utf-8') as f:
        f.write(log)


delete(-1)


# Задача 7. Реализуйте процедурную генерацию спрайтов 5x5 пикселей
# с помощью Matplotlib и функции imshow.
def square_gen():
    square = [[0 for column in range(5)] for row in range(5)]
    for i in range(5):
        for j in range(3):
            square[i][j] = rand.randint(0, 1)
            if square[i][j] == 1 and j != 2:
                square[i][4 - j] = 1
    return square


def square_show(square):
    res = np.zeros((5, 5, 3))
    for i in range(5):
        for j in range(5):
            if square[i][j] == 1:
                res[i][j] = [255, 255, 255]
    return res


def main():
    fig, axes = plt.subplots(nrows=20, ncols=20)
    for ax in axes.flat:
        ax.imshow(square_show(square_gen()))
        ax.axis('off')
    plt.show()


# main()


# Задача 11. Проанализируйте базу данных старых компьютерных игр.
def games():
    j = 0
    years = []
    listing = []
    with open('GAMES.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            z = "".join(row)
            listing.append(z)
    mes = listing
    for i in mes:
        temple_str = ''.join(i).split(';')
        if temple_str[3].strip('"') != "не издана":
            if int(temple_str[3].strip('"')) not in years:
                years.append(int(temple_str[3].strip('"')))
    popular = [0] * len(years)
    for i in mes:
        temple_str = ''.join(i).split(';')
        if temple_str[3].strip('"') != "не издана":
            if years[j] == int(temple_str[3].strip('"')):
                popular[j] += 1
            else:
                j += 1
                popular[j] += 1
    plt.bar([str(i) for i in years], popular)
    plt.title('Распределение игр по популярности выхода')
    plt.show()
    themes = []
    for i in mes:
        temple_str = ''.join(i).split(';')
        if temple_str[1].strip('"') not in themes:
            themes.append(temple_str[1].strip('"'))
    data = {i: [0] * len(years) for i in sorted(themes)}
    for i in mes:
        temple_str = ''.join(i).split(';')
        if temple_str[3].strip('"') != "не издана":
            data[temple_str[1].strip('"')][
                years.index(int(temple_str[3].strip('"')))] += 1
    for k, v in data.items():
        plt.plot(years, v, label=k)
    plt.legend(data, loc=2)
    plt.show()


# games()
