import random
import math


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def mul(a, b, m):
    if b == 1:
        return a
    if b % 2 == 0:
        t = mul(a, b // 2, m)
        return (2 * t) % m
    return (mul(a, b - 1, m) + a) % m


def pows(a, b, m):
    if b == 0:
        return 1
    if b % 2 == 0:
        t = pows(a, b // 2, m)
        return mul(t, t, m) % m
    return (mul(pows(a, b - 1, m), a, m)) % m


def ferma(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for _ in range(100):
        a = random.randint(2, x - 1)
        if gcd(a, x) != 1:
            return False
        if pows(a, x - 1, x) != 1:
            return False
    return True


def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    t = n - 1
    s = 0

    while t % 2 == 0:
        t //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pows(a, t, n)

        if x == 1 or x == n - 1:
            continue

        for r in range(1, s):
            x = pows(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break

        if x != n - 1:
            return False
    return True


def solovei_shtrassen_test(n, k):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        if gcd(n, a) > 1:
            return False

        b = (n - 1) // 2
        x = pows(a, b, n)

        if x == jacobi(a, n):
            return True
        else:
            return False
    return True


def jacobi(a, n):
    k = 0
    s = 1
    a1 = a
    if a == 0:
        return 0
    if a == 1:
        return 1
    while a1 % 2 == 0:
        k += 1
        a1 //= 2
    if k % 2 == 0:
        s = 1
    elif n % 8 in [1, 7]:
        s = 1
    else:
        s = -1
    if n % 4 == 3 and a1 % 4 == 3:
        s = -s
    if a1 == 1:
        return s
    else:
        return jacobi(n % a1, a1)


if __name__ == "__main__":
    n = int(input("Введите число, которое надо проверить: "))
    while True:
        choice = int(input(
            "Выберите способ, которым хотите реализовать проверку числа:\n1. Тест Ферма\n2. Тест Соловея-Штрассена\n3. Тест Миллера-Рабина\n"))
        if choice == 1:
            print("Число простое" if ferma(n) else "Число не простое")
        elif choice == 2:
            k = int(input("Введите количество проверок k: "))
            print("Число простое" if solovei_shtrassen_test(n, k) else "Число не простое")
        elif choice == 3:
            k = int(input("Введите количество проверок k: "))
            print("Число простое" if miller_rabin_test(n, k) else "Число не простое")

        choice2 = int(input("Хотите ли вы проверить еще одним методом?\n1. Да\n2. Нет\n"))
        if choice2 == 2:
            break