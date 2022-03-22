import random as r

# lab_03
# zadanie 1

a = [1-i for i in range(1, 11)]
print(a)

b = [4 ** i for i in range(8)]
print(b)

c = [i for i in b if i % 2 == 0]
print(c)


# zadanie 2

lista1 = [r.randint(0, 20) for i in range(11)]
print(lista1)

lista2 = [i for i in lista1 if i % 2 == 0]
print(lista2)


# zadanie 3

zakupy = {"szt.": "Baton Mars",
          "kg": "Banan",
          "ml": "Mleko"}

nowe = {}
for key, value in zakupy.items():
    nowe[value] = key
print(nowe)

# zadanie 4

def prosto(a, b, c):
    if (a ** 2 + b ** 2) == c ** 2:
        print("trojkat jest prostokatny")
    else:
        print("trojkat nie jest prostokatny")

prosto(3, 4, 6)

# zadanie 5

def trap(a = 1, b = 2, h = 1):
    return ((a + b) * h) / 2

print(trap())

# zadanie 6

def ciag(a = 1, b = 4, n = 10):
    if a == 0:
        return 0
    licz = a
    temp = a
    for i in range(n - 1):
        temp *= b
        licz *= temp
    return licz

print(ciag(1, 3, 3))

# zadanie 7

def ciagwiazdka(* l):
    if l[0] == 0:
        return 0
    licz = l[0]
    temp = l[0]
    for i in range(l[2] - 1):
        temp *= l[1]
        licz *= temp
    return licz

print(ciagwiazdka(1, 3, 3))

# zadanie 8

def zak(** zakup):
    for i in zakup:
        print(i + "\t- {0:.2f}".format(zakup[i]) + "\tzł")

zak(mleko=3.14,maka=50.00,chleb=75.00)

# zadanie 9

from ciagawa import *

print(arytm.n(1, 1, 50))
print(geome.sn(1, 2, 5))