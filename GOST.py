from random import randint
import math as mt

def test_ferma(n, t):
    for i in range(t):
        a = randint(2, n - 2)
        r = pow(a, n - 1, n)  
        if r != 1:
            return False
    return True

def Jacobi(a, n):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    s = 0
    k = 0
    a1 = a
    if a % 2 == 0:
        while a1 % 2 == 0:
            k += 1
            a1 //= 2 
    if k % 2 == 0:
        s = 1
    elif n % 8 == 1 or n % 8 == 7:
        s = 1
    else:
        s = -1
    if n % 4 == 3 and a1 % 4 == 3:
        s = -s
    if a1 == 1:
        return s
    else:
        return s * Jacobi(n % a1, a1)

def test_solovey_shtrassen(n, t):
    for i in range(t):
        a = randint(2, n - 2)
        r = pow(a, (n - 1) // 2, n) 
        if r != 1 and r != n - 1:
            return False
        s = Jacobi(a, n)
        if r != (s % n):
            return False
    return True

def test_miller_rabin(n, t):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    for _ in range(t):
        b = randint(2, n - 2)
        y = pow(b, r, n)  
        if y != 1 and y != n - 1:
            j = 1
            while j < s and y != n - 1:
                y = pow(y, 2, n)  
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True

def gost_alg(t, q):
    k = 0
    y = randint(1, 65535)
    c = randint(1, 65535)
    r = t // 16
    while True:
        Y = 0
        for i in range(r):
            Y += y * pow(2, 16 * i)
            y = (19381 * y + c) % pow(2, 16)
        eps = Y / pow(2, 16 * r)
        N = mt.ceil(pow(2, t - 1) / q) + int(pow(2, t - 1) / q * eps)
        u = 0
        while True:
            p = q * (N + u) + 1
            if p > pow(2, t):
                break
            if pow(2, p - 1, p) == 1 and pow(2, N + u, p) != 1:  
                return p
            else:
                u += 2

iterations = 100
count1 = 0
count2 = 0
count3 = 0
big_massive = []

for j in range(10):
    massive = [gost_alg(18, 257) for i in range(10)]
    big_massive.extend(massive)
    for i in range(len(massive)):
        if test_ferma(massive[i], iterations):
            count1 += 1
        if test_solovey_shtrassen(massive[i], iterations):
            count2 += 1
        if test_miller_rabin(massive[i], iterations):
            count3 += 1
    print(big_massive)
    print(f"Тест Ферма: ", count1)
    print(f"Тест Соловея-Штрассена: ", count2)
    print(f"Тест Миллера-Рабина: ", count3)