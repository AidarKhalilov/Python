import copy


# Печать матрицы
def printmatrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end=' ')
        print('\n', end='')


# Сумма матриц
def add(a, b):
    result = copy.copy(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] + b[i][j]
    return result


# Произведение Адамара
def multiply(a, b):
    result = copy.copy(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j] * b[i][j]
    return result


# Элемент матрицы для произведения
def element(a, b, i, j):
    elem = 0
    for k in range(len(a[0])):
        elem += a[i][k] * b[k][j]
    return elem


# Произведение матриц
def dot(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            c = element(a, b, i, j)
            row.append(c)
        result.append(row)
    return result


# Транспонирование матрицы, исправлено
def transpose(a):
    result = []
    for i in range(len(a[0])):
        result.append([])
        for j in range(len(a)):
            result[i].append(a[j][i])
    return result


# Подматрица для минора
def submatrix(a, first, second):
    result = []
    for i in range(len(a)):
        if i == first:
            continue
        row = []
        for j in range(len(a[i])):
            if j == second:
                continue
            row.append(a[i][j])
        result.append(row)
    return result


# Минор матрицы 2 х 2
def smalldet(a):
    return a[0][0]*a[1][1] - a[0][1] * a[1][0]


# Определитель произвольной матрицы
def det(a, i=0):
    if len(a) == 2:
        return smalldet(a)
    result = 0
    for j in range(len(a)):
        value = (-1) ** (j + i) * a[i][j] * det(submatrix(a, i, j), 0)
        result += value
    return result


# Минор произвольный
def minor(a, i, j):
    c = submatrix(a, i, j)
    result = det(c)
    return result


# Алгебраическое дополнение
def alg(a, i, j):
    return (-1) ** (j + i) * minor(a, i, j)


# Матрица алгебраических дополнений
def algmatrix(a):
    result = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[i][j] = alg(a, i, j)
    return result


# Обратная матрица
def inv(a):
    first = transpose(algmatrix(a))
    second = det(a)
    for i in range(len(a)):
        for j in range(len(a[i])):
            first[i][j] /= second
    return first


printmatrix(inv([[0, 2, 1, 4], [1, 0, 3, 2], [0, 1, 4, 0], [1, 2, 1, 1]]))
