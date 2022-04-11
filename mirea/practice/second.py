import random
import sys

# Задача 1

vowels = ['а', 'о', 'у', 'э', 'ы', 'е', 'ё', 'ю', 'я']
consonant = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
             'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
names = open('C:/Users/Home/Downloads/male_names_rus.txt', 'r', encoding='utf-8').read().splitlines()


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
# sys.stdout.write(myprint({'first': 1, 'second': 2}, 'Hello World!', 123, 'H', 0.565, sep='\n'))


def surnames_generator(m):
    surname = ''
    while m != 0:
        for j in range(random.randint(6, 12)):
            if j % 2 == 0:
                surname =
