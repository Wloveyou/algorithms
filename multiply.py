import numpy as np


# Алгоритм Кацубы для чисел
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    sx = str(x)
    sy = str(y)
    n = max(len(sx), len(sy))
    half_n = n // 2

    a = int(sx[:-half_n]) if half_n < len(sx) else 0
    b = int(sx[-half_n:]) if half_n < len(sx) else int(sx)
    c = int(sy[:-half_n]) if half_n < len(sy) else 0
    d = int(sy[-half_n:]) if half_n < len(sy) else int(sy)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)
    return ac * (10 ** (2 * half_n)) + (abcd - ac - bd) * (10 ** half_n) + bd


def strassen(A, B):
    n = len(A)
    if n <= 2:
        C = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    mid = n // 2
    A11 = np.array([row[:mid] for row in A[:mid]])
    A12 = np.array([row[mid:] for row in A[:mid]])
    A21 = np.array([row[:mid] for row in A[mid:]])
    A22 = np.array([row[mid:] for row in A[mid:]])

    B11 = np.array([row[:mid] for row in B[:mid]])
    B12 = np.array([row[mid:] for row in B[:mid]])
    B21 = np.array([row[:mid] for row in B[mid:]])
    B22 = np.array([row[mid:] for row in B[mid:]])

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = np.zeros((n, n), dtype=int)
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22
    return C


def toom_cook(x, y):
    if x < 10 or y < 10:
        return x * y

    m = 3

    x_digits = [int(d) for d in reversed(str(x))]
    y_digits = [int(d) for d in reversed(str(y))]

    while len(x_digits) % m != 0:
        x_digits.append(0)
    while len(y_digits) % m != 0:
        y_digits.append(0)

    x_parts = [sum(digit * (10 ** i) for i, digit in enumerate(x_digits[j:j + m]))
               for j in range(0, len(x_digits), m)]
    y_parts = [sum(digit * (10 ** i) for i, digit in enumerate(y_digits[j:j + m]))
               for j in range(0, len(y_digits), m)]

    n = max(len(x_parts), len(y_parts))
    x_parts = x_parts + [0] * (n - len(x_parts))
    y_parts = y_parts + [0] * (n - len(y_parts))

    p = [0, 1, -1, 2, float('inf')]
    v = []

    for px in p:
        xv = sum(x_part * (px ** i) for i, x_part in enumerate(x_parts))
        yv = sum(y_part * (px ** i) for i, y_part in enumerate(y_parts))
        v.append(xv * yv)

    z0 = v[0]
    z1 = (4 * v[1] - v[2] - 3 * v[0]) / 2
    z2 = (-2 * v[1] + 2 * v[2]) / 2
    z3 = (4 * v[2] - v[1] - 3 * v[3]) / 6
    z4 = (v[1] + v[3] - 2 * v[2]) / 24

    z = sum(int(round(z_i * (10 ** (i * m)))) for i, z_i in enumerate([z0, z1, z2, z3, z4]))

    return int(z)


x = 11
y = 28

print("Метод Карацубы:", karatsuba(x, y))
print("Метод Тоома-Кука:", toom_cook(x, y))
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("Метод Штрассена:n", strassen(matrix1, matrix2))

matrix3 = np.array([[1]])
matrix4 = np.array([[2]])
print("Метод Штрассена:n", strassen(matrix3, matrix4))