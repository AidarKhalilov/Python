def getfirst(x):
    return x & 0x00ff


def getsecond(x):
    x &= 0xfff00
    return x >> 8


def getthird(x):
    x &= 0x1f00000
    return x >> 20


def getfourth(x):
    x &= 0x3e000000
    return x >> 25


def getfifth(x):
    x &= 0xc0000000
    return x


def merge(y):
    x = getfifth(y)
    x = x | (getfirst(y) << 22)
    x = x | (getsecond(y) << 10)
    x = x | (getfourth(y) << 5)
    x = x | getthird(y)
    return x


def main(x):
    return merge(x)


# print(hex(main(0x6b98bedd)))

