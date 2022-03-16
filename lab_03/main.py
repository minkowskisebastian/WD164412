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