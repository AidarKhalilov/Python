import re


def delete_rows(x): # Удаление дублей среди строк
    i = 0
    n = len(x)
    while i != n:
        current_value = x[i][0]
        j = i + 1
        while j != n:
            if x[j][0] == current_value:
                x.pop(j)
                j -= 1
                n -= 1
            j += 1
        i += 1
    return x


def delete_empty_rows(x): # Удаление пустых строк
    i = 0
    n = len(x)
    while i != n:
        if x[i][0] is None:
            x.pop(i)
            n -= 1
        i += 1
    return x


def convert_date(x): # Преобразование данных в таблице
    n = len(x)
    for i in range(n):
        for j in range(n):
            if j == 0:
                x[i][j] = re.search(r'\w+\.\w+', x[i][j]).group()
            elif j == 1:
                if x[i][j] == 'N':
                    x[i][j] = 0
                else:
                    x[i][j] = 1
            else:
                result = x[i][j].split(sep = '/')[::-1]
                x[i][j] = '.'.join(result)
    return x


def transpose(x): # Транспонирование таблицы
    result = []
    for i in range(len(x[0])):
        result.append([])
        for j in range(len(x)):
            result[i].append(x[j][i])
    return result


def main(x):
    x = delete_rows(x)
    x = delete_empty_rows(x)
    x = convert_date(x)
    x = transpose(x)
    return x


print(main([['redivide6[at]yandex.ru', 'N', '04/04/08'],
                   ['redis7[at]mail.ru', 'Y', '99/04/16'],
                   [None, None, None],
                   ['limberer58[at]yahoo.com', 'N', '99/12/24'],
                   ['limberer58[at]yahoo.com', 'N', '99/12/24'],
                   ['limberer58[at]yahoo.com', 'N', '99/12/24']]))
