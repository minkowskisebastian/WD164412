import numpy as np
import math
import random as r

# lab_06

# zadanie 1

a = np.arange(3)
b = np.arange(4, 3 * 4 + 1, 4)
print(a * b)


# zadanie 2

a2 = np.arange(5, 5*9+1, 5).reshape((3, 3))
b2 = np.arange(16).reshape((4, 4))

print(np.amin(a2, axis=0))
print(np.amin(a2, axis=1))
print(np.amin(b2, axis=0))
print(np.amin(b2, axis=1))


# zadanie 3

print(a.dot(b.T))


# zadanie 4

a4 = np.array((1, 2, 3))
a5 = np.array((math.e, 2.50, 21.37))
print(a4 * a5)


# zadanie 5

c = np.zeros((2, 3))

for i in range(2):
    for j in range(3):
        c[i][j] = r.randint(0, 100)

a = np.sin(c)
print(a)


# zadanie 6

b = np.cos(c)
print(b)


# zadanie 7

print(a + b) # (???)


# zadanie 8

e = np.arange(3, 3 * 9 + 1, 3).reshape((3, 3))

for i in e:
    print(i)


# zadanie 9

for i in e.flat:
    print(i)


# zadanie 10

w = np.arange(81).reshape((9, 9))
print(w)

w = np.reshape(w, newshape=(27,3))
print(w)

# wielkość macierzy musi się zgadzać z ilością elementów dlatego w przykładzie 9 * 9 = 81 = 27 * 3


# zadanie 11

o = np.arange(12).reshape((3, 4))
o2 = np.reshape(o, newshape=(4, 3))
o3 = np.reshape(o, newshape=(2, 6))

for i in o.flat:
    print(i)

for i in o2.flat:
    print(i)

for i in o3.flat:
    print(i)

# wyniki są takie same
