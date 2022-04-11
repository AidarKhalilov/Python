import decimal
from decimal import Decimal


def delete_column(x, index):
    for i in range(len(x)):
        x[i].pop(index)
    return x


def delete_double_column(x):
    for i in range(len(x[0])):
        currentValue = x[0][i]
        for j in range(i + 1, len(x) - 1):
            if x[0][j] == currentValue:
                return delete_column(x, j)


def delete_row(x, index):
    x.pop(index)
    return x


def delete_double_row(x):
    for i in range(len(x)):
        currentValue = x[i][0]
        for j in range(i + 1, len(x)):
            if x[j][0] == currentValue:
                return delete_row(x, j)


def convert(x):
    for i in range(len(x[0])):
        for j in range(len(x)):
            match i:
                case 0:
                    x[j][i] = x[j][i].replace(' ', '(', 1)
                    x[j][i] = x[j][i].replace(' ', ')', 1)
                case 1:
                    x[j][i] = str(Decimal(float(x[j][i]) * 100).
                                  quantize(Decimal('1'), decimal.ROUND_HALF_UP)) \
                              + '%'
                case 2:
                    if x[j][i] == 'Y':
                        x[j][i] = 'true'
                    else:
                        x[j][i] = 'false'
    return x


def operations(x):
    x = delete_double_column(x)
    x = delete_double_row(x)
    x = convert(x)
    return x


def main(x):
    return operations(x)
