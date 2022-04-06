import numpy as np

# zadanie 1

a = np.arange(4, 81, 4)
print(a)


# zadanie 2

b = np.arange(1.0, 2.0, 0.12, dtype='float')
c = b.astype('int32')
print(c)
print(c.shape)
print(c.dtype)
print(c.ndim)


# zadanie 3

def pot(n: int):
    m = np.identity(n, int)
    for i in range(n):
        for j in range(n):
            m[i, j] = 2 ** (i + j)
    return m


print(pot(5))


# zadanie 4

def generuj(n, m):
    a = np.arange(m)
    for i in range(m):
        a[i] = n ** (i + 1)
    return a


print(generuj(3, 5))


# zadanie 5

def odwr(n: int):
    v = [n - i for i in range(n)]
    return np.diag([i for i in v],2)


print(odwr(5))

# zadanie 6
