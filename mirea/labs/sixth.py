def LEFTfirst(x):
    if x[0] == 1990:
        return LEFTsecondleft(x)
    else:
        return 4


def LEFTsecondleft(x):
    if x[2] == 'GO':
        return 0
    else:
        return LEFTthirdright(x)


def LEFTthirdright(x):
    if x[4] == 1981:
        return 1
    elif x[4] == 1982:
        return 2
    else:
        return 3


# Правая ветка
def RIGHTfirst(x):
    if x[1] == 2000:
        return RIGHTsecondleft(x)
    else:
        return RIGHTsecondright(x)


def RIGHTsecondleft(x):
    if x[2] == 'GO':
        return 5
    else:
        return RIGHTthirdright(x)


def RIGHTthirdright(x):
    if x[0] == 1990:
        return 6
    else:
        return 7


def RIGHTsecondright(x):
    if x[0] == 1990:
        return RIGHTthirdRIGHT(x)
    else:
        return 10


def RIGHTthirdRIGHT(x):
    if x[2] == 'GO':
        return 8
    else:
        return 9


def f(x):
    if x[3] == 2020:
        return LEFTfirst(x)
    else:
        return RIGHTfirst(x)


def main(x):
    return f(x)
