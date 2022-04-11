def diff_ways():
    assert 42 == 0b101010  # Двоичная система счисления
    assert 42 == 0x2a  # Шестнадцатеричная система счисления
    assert 42 == 0o52  # Восьмеричная система счисления
    assert 42 == 42.0  # Вещественное представление числа
    assert 42 == 42 + 0j  # Комплексное представление числа
    assert 42 == 42e0  # 42 * 10 ^ 0
    assert 42 == 84 >> 1  # Битовые операции
    assert 42 == 21 << 1  # Битовые операции
    assert 42 == 42 & 42  # Битовые операции
    assert 42 == 42 | 0  # Битовые операции
    # divmod(a,b) - возвращает пару чисел


def easter_eggs():
    # antigravity - комиксы
    # import this
    # import __hello__
    # from __future__ import braces
    pass


def fourth(x, y, z, k):
    x = x + x  # Умножение на 12
    x = x + x
    x = x + x + x
    y = y + y  # Умножение на 16
    y = y + y
    y = y + y
    y = y + y
    z1 = z  # Умножение на 15
    z = z + z
    z = z + z
    z = z + z
    z2 = z1 - z
    z = z - z2
    k1 = k
    k = k + k  # Умножение на 29
    k = k2 = k + k
    k = k + k
    k = k + k
    k = k + k
    k = k - k2 + k1
    return x, y, z, k


def errors():
    pass
    # assert 0.6 + 0.3 == 0.9
    # (True * 2 + False) * -True [(1 * 2 + 0) * -1]
    # 1 = input("Enter a name")
    # result--
    # return foo()
    # return "hello world" - "world"
    # return 1 / 0
    # return math.log(-1)
    # return 1-math.exp(-4*1000000*-0.0641515994108)


def naive_mul(x, y):
    result = 0
    for i in range(0, y):
        result += x
    return result


def fast_mul(x, y):
    first = []
    second = []
    result = 0
    while x != 0:
        first.append(x)
        second.append(y)
        x = x // 2
        y = y * 2
    for i in range(len(first)):
        if first[i] % 2 == 1:
            result += second[i]
    return result


def fast_pow(x, y):
    first = []
    second = []
    result = 1
    while y != 0:
        first.append(x)
        second.append(y)
        x = x ** 2
        y = y // 2
    for i in range(len(second)):
        if second[i] % 2 == 1:
            result *= first[i]
    return result


def test():
    for i in range(0, 101):
        for j in range(0, 101):
            assert fast_pow(i, j) == i**j
            assert fast_mul(i, j) == i*j
            assert naive_mul(i, j) == i*j


def fast_mul_gen(y):
    print("def f(x):")
    print("\ts = 0")
    n = 1
    while y != 0:
        print("\t" + ("x1 = x" if n // 2 == 0 else "x" + str(n) + " = x" + str(n // 2) + " + x" + str(n // 2)))
        if y % 2 == 1:
            print("\ts += x" + str(n))
        y //= 2
        n *= 2
    print("\treturn s")


def fast_pow_gen(y):
    print("def f(x):")
    print("\tp = 1")
    n = 1
    while y != 0:
        print("\t" + ("x1 = x" if n // 2 == 0 else "x" + str(n) + " = x" + str(n // 2) + " * x" + str(n // 2)))
        if y % 2 == 1:
            print("\tp *= x" + str(n))
        y //= 2
        n *= 2
    print("\treturn p")


def task11():
    fast_mul_gen(int(input("Введите число для тестирования умножения из 11 задания: ")))
    fast_pow_gen(int(input("Введите число для тестирования возведения в степень из 11 задания: ")))


task11()
