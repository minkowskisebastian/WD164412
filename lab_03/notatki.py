# lab_03
# notatki z zajec

import math as m

# 1. skrocone petle

a = [i ** 2 for i in range(10)]
print(a)

a2 = []
for i in range(10):
    a2.append(i ** 2)
print(a2)

b = [3 ** i for i in range(6)]
print(b)

b2 = []
for i in range(6):
    b2.append(3 ** i)
print(b2)

c = [i for i in a if i % 2 != 0]
print(c)

c2 = []
for i in a:
    if i % 2 != 0:
        c2.append(i)
print(c2)

# 2. zagnieżdżenie

lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a, b))
print(lista)

lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
print(lista2)

# 3. działania na słownikach

slownik = {'PKO': 'Państwowa Kasa Oszczędności',
           'PZU': 'Państwowy Zakład Ubezpieczeń'}
print(slownik)

slownik_odwr = {}
for key, value in slownik.items():
    slownik_odwr[value] = key
print(slownik_odwr)


# 4. funkcje

# def nazwa_funkcji(argumenty warunki i ten tego):
#     instrukcja
#     return

def row_kwadratowe(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("brak rozwiązań")
        return -1
    elif delta == 0:
        print('jedno rozwiązanie')
        x = (-b) / (2 * a)
        return x
    else:
        print("dwa rozwiązania")
        x1 = (-b - m.sqrt(delta)) / (2 * a)
        x2 = (-b + m.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 2))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 5, 3))


def parzyste(n):
    if n % 2 == 0:
        print("liczba n jest parzysta")
        return 1
    else:
        print("liczba n jest nieparzysta")
        return 0


parzyste(4)
parzyste(7)


def dl(x1=1, y1=2, x2=3, y2=4):
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# argumenty domyślne
print(dl())

# argumenty pozycyjne
print(dl(4, 5, 6, 10))

# dwa pierwsze argumenty pozycyjne, kolejne dwa wpisywane wartości
print(dl(1, 1, y2=8, x2=7))

# wartość przypisana do danego argumentu
print(dl(y2=3, x1=5, y1=6, x2=0))

# wartości domyślne i dwie nowe wartości
print(dl(y2=10, x2=10))


def ciag(* liczba):
    if len(liczba) == 0:
        return 0
    else:
        suma = 0
        for i in liczba:
            suma += i
        return suma


print(ciag())
print(ciag(1, 2, 3, 4, 5, 6, 7, 8))


def co_lubie(** things):
    for smth in things:
        print("lubie " + str(smth) + " a dokładnie:")
        print(things[smth])


co_lubie(gry=['planszowe', 'komputerowe'])
