import itertools
import random
import re
import sys
from itertools import groupby


# Задача 1
def first(s):
    return [int(elem) for elem in s]


def second(s):
    return len(set(s))


def third(s):
    return s[::-1]


def fourth(s, x):
    return [i for i in range(len(s)) if s[i] == x]


def fifth(s):
    return sum(s[i] for i in range(len(s)) if i % 2 == 0)


def sixth(s):
    return max(s)


# Задача 2
def seventh(i):
    x = 'much', 'c', 'w'
    return x[i]


# Задача 3
def generate_groups(chars):
    result = []
    row = []
    for j in range(len(chars)):
        match chars[j]:
            case 'В':
                for i in range(1, 9):
                    row.append('ИВБО-0' + str(i) + '-20')
                row.append('ИВБО-13-20')
                result.append(row)
                row = []
            case 'К':
                for i in range(1, 28):
                    if i < 10:
                        row.append('ИКБО-0' + str(i) + '-20')
                    else:
                        row.append('ИКБО-' + str(i) + '-20')
                row.append('ИКБО-30-20')
                result.append(row)
                row = []
            case 'Н':
                for i in range(1, 12):
                    if i < 10:
                        row.append('ИНБО-0' + str(i) + '-20')
                    else:
                        row.append('ИНБО-' + str(i) + '-20')
                row.append('ИНБО-13-20')
                row.append('ИНБО-15-20')
                result.append(row)
                row = []
            case 'М':
                for i in range(1, 3):
                    row.append('ИМБО-0' + str(i) + '-20')
                result.append(row)
                row = []
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j])
        print('\n')


# generate_groups(['В', 'К', 'Н', 'М'])


# Задача 4. Объяснить [0xfor _ in 'abc']
# Сначала парсится шестнадцатеричный литерах до 0xf = 15
# Затем парсится часть or _ in 'abc', проверка есть ли символ _ в строке abc
# Но так как левое выражение всегда True, правое выражение не играет роли (Short circuit evaluation)


# Задача 5. Реализуйте генератор докладов по цифровой экономике
def generate_reports():
    result = [['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее', 'Следовательно,',
               'Соответственно,', 'Вместе с тем,', 'С другой стороны,'],
              ['парадигма цифровой экономики', 'контекст цифровой трансформации',
               'диджитализация бизнес-процессов', 'прагматичный подход к цифровым платформам',
               'совокупность сквозных технологий', 'программа прорывных исследований',
               'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data'],
              ['открывает новые возможности для', 'выдвигает новые требования', 'несёт в себе риски',
               'расширяет горизонты', 'заставляет искать варианты', 'не оставляет шанса для',
               'повышает вероятность', 'обостряет проблему'],
              ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта',
               'компрометации конфиденциальных', 'универсальной коммодитизации',
               'несанкционированной кастомизации', 'нормативного регулирования',
               'практического применения'
               ], ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.',
                   'опасных экспериментов.', 'государственно-частных партнёрств.',
                   'цифровых следов граждан.', 'нежелательных последствий.', 'внезапных открытий.']]
    reports = ''
    for i in range(8):
        for j in range(5):
            reports += result[j].pop(random.randint(0, len(result[j]) - 1)) + ' '
        reports += '\n'
    return reports


# print(generate_reports())


# Задача 6. Функция print()
def myprint(*args, sep=' '):
    return sep.join([str(i) for i in args])


# Задача 7. Функция именованных аргументов
def foo(*, length, name='Айдар', surname='Халилов'):
    return name + ' ' + surname + length


# Задача 8. Генератор фамилий
def generate_surnames():
    pass


# Задача 9. Объясните «странности» в следующих примерах
# a = 1
# b = 1
# c = 300000 # проверено в Python 3.10
# d = 300000
# print(a is b, c is d)
# a, b = 'py', 'py'
# c = ''.join(['p', 'y'])
# print(a is b, a == c, a is c)
# На самом деле, чтобы сэкономить время и память,
# Python всегда предварительно загружает все маленькие целые числа
# в диапазоне [-5, 256]. Когда объявляется новая целочисленная переменная
# в этом диапазоне, Python просто ссылается на нее из кэшированного целого числа
# и не создает никакого нового объекта.
# Когда переменным a и b были присвоены 300000, они стали двумя разными объектами
# в разных местах памяти, потому что 300000 не находится в диапазоне кэширования малых целых чисел.
# Мы также можем использовать функцию id(), которая печатает местоположение переменной в памяти,
# чтобы подтвердить приведенные выше объяснения:
# a = 256
# b = 256
# id(a) == id(b)
# True
# a = 257
# a = 257
# id(a) == id(b)
# False

# Задача 6. Реализуйте функцию print()
sys.stdout.write(myprint({'first': 1, 'second': 2}, 'Hello World!', 123, 'H', 0.565, sep=''))
print('')

# Задача 12. Замена кавычек в markdown файле
def change_markdown():
    # Считать файл как целую строку
    with open('readme.md', 'r', encoding = 'utf-8') as f:
        str = f.read()
    flag = True
    for i in range(len(str)):
        if str[i] == '"' and flag == True:
            str = str.replace('"', '«', 1)
            flag = False
        elif str[i] == '"' and flag == False:
            str = str.replace('"', '»', 1)
            flag = True
        else:
            continue

    # Записать новую информацию в файл
    with open("readme.md", 'w', encoding='utf-8') as f:
        f.write(str)
    return True


def random_something(name_of_file):
    with open(name_of_file, 'r', encoding='utf-8') as f:
        lines =[]
        for line in f:
            lines.append(line)
        random_profession = random.choice([line.rstrip() for line in lines])
    return random_profession


# Задача 8. Генератор фамилий
def generate_surnames(number_of_names = 10):
    surname = ''
    ending = ['ов', 'ев', 'ин', 'ых', 'ой']
    for i in range(number_of_names):
        name = random_something('names.txt')
        profession = random_something('profession.txt')
        property = random_something('properties.txt')
        quality = random_something('qualities.txt')
        rand = random.choice([name, profession, property, quality])
        if rand == profession:
            surname = rand + ending[0] + ' ' + random_something('names.txt') + ' ' + \
                      random_something('alphabet.txt') + '.'
        elif rand == property:
            surname = rand[:-2] + ending[3] + ' ' + random_something('names.txt') + ' ' + \
                      random_something('alphabet.txt') + '.'
        elif rand == quality:
            surname = rand + ending[4] + ' ' + random_something('names.txt') + ' ' + \
                      random_something('alphabet.txt') + '.'
        else:
            surname = rand + ending[random.randint(0, len(ending) - 3)] + ' ' + random_something('names.txt') + ' ' + \
                      random_something('alphabet.txt') + '.'
        yield surname


# Задача 11. Преобразования Барроуза-Уиллера
def bwt(data):
    result = ''
    sorted_list = sorted(cycle_permutations(data))
    n = len(data)
    for i in range(n):
        result += sorted_list[i][n - 1]
        if sorted_list[i] == data:
            number_in_list = i
    return result, number_in_list


# Обратное преобразование
def inverse_bwt(tuple):
    result = [i for i in sorted(tuple[0])]
    n = len(tuple[0])
    for i in range(n - 1):
        for j in range(n):
            result[j] = tuple[0][j] + result[j]
        result = sorted(result)
    return result[tuple[1]]


# Циклические перестановки для задачи 11
def cycle_permutations(data):
    result = [data]
    for i in range(len(data) - 1):
        data = data[1:] + data[0]
        result.append(data)
    return result


def rle_encode(data):
    return [(k, len(list(g))) for k, g in groupby(data)]


print(rle_encode('абракадабра'))
print(inverse_bwt(bwt('абракадабра')))


# Задача 10. Интеллектуальный разбор
def parse_subj(text):
    parse_group = re.search(r'[КВНМквнмkvbnKVBN](?=[Бб])|[КВНМквнмkvbnKVBN](?=[\s_-]*\d)', text)
    group = ''
    number = ''
    variant = ''
    if parse_group is not None:
        match(parse_group.group()):
            case 'к': group = 'ИКБО'
            case 'н': group = 'ИНБО'
            case 'в': group = 'ИВБО'
            case 'м': group = 'ИМБО'
            case 'k': group = 'ИКБО'
            case 'v': group = 'ИВБО'
            case 'm': group = 'ИМБО'
            case 'n': group = 'ИНБО'
            case 'К': group = 'ИКБО'
            case 'В': group = 'ИВБО'
            case 'Н': group = 'ИНБО'
            case 'М': group = 'ИМБО'
            case 'K': group = 'ИКБО'
            case 'B': group = 'ИВБО'
            case 'V': group = 'ИВБО'
            case 'M': group = 'ИМБО'
            case 'N': group = 'ИНБО'
    parse_number = re.search(r'(?<=[КМНВкмнвkvnmKVBNM])\d{1,2}|(?<=И[КМНВкмнвkvnmKVNM]БО-)\d{1,2}|'
                             r'(?<=[КМНВкмнвkvnmKVNM]\s)\d{1,2}|(?<=[КМНВкмнвkvnmKVNM]-)\d{1,2}', text)
    if parse_number is not None:
        if len(parse_number.group()) == 1:
            number = '-0' + parse_number.group() + '-20'
        else:
            number = '-' + parse_number.group() + '-20'
    parse_variant = re.search(r'\d{1,2}$', text)
    if parse_variant is not None:
        variant = parse_variant.group()
    if group != '' and number != '' and variant != '':
        return group + number + '. Вариант: ' + variant
    else:
        return None


def main(text):
    result = []
    not_parsed = 0
    for i in range(len(text)):
        rez = parse_subj(text[i])
        if rez is not None:
            result.append(rez)
        else:
            not_parsed += 1
    return result, not_parsed


print(main(['main.py', 'k17 14', 'K13 18', 'к02 1', 'ИВБО-11 Вариант№14',
            'к02 21', '1.3.py', 'В 11 4', '\ufeff\u200b\u200bк20 21', 'B7 21',
            'Фамилия Имя Задача 1.1', 'В03 12', 'к08 24', 'к07 23', '1.2.py, 1.3.py, 1.4.py',
            '1.1.py', 'K14 23', 'в7 ', 'к6 ', '\u200b\u200bк20 21', 'к2 в3', 'В104', 'В1013',
            'B3 29', 'v10 15', 'k13 30', 'В 7 10', 'Фамилия И.О. к7 31', '1.2.py', 'К10',
            'ПитонН4 н11', 'K13 28', 'К4', 'K17 10', 'и4 11', 'Н1', 'н01 28', 'б3 5',
            'Re: в6 28', 'к-11 3', '2_1.py, 2_2.py']))