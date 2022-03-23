# lab_04

import random

# zadanie 1

lista1 = [random.randint(0, 30) for i in range(11)]
lista2 = [i * 2 for i in lista1]
print(lista1)
print(lista2)

wynik = open("wynik.txt", "w+")
wynik.writelines(str(lista2))
wynik.close()

# zadanie 2

wynik = open("wynik.txt", "r")
print(wynik.readline())
wynik.close()

# zadanie 3

n = input("ile? ")

with open("bomba.txt", "w+") as f:
    for i in range(int(n)):
        f.write(input())
        f.write("\n")

with open("bomba.txt", "r") as f:
    for i in f:
        print(i, end="")


# zadanie 4

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa: " + self.nazwa_produktu)
        print("Ilość: " + str(self.ilosc))
        print("Cena za 1" + self.jednostka_miary + " " + "%(c).2f" % {'c': self.cena_jed} + "zł")

    def ile_produktu(self):
        print(self.nazwa_produktu + " - " + str(self.ilosc) + self.jednostka_miary)

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed


Banan = NaZakupy("Banan", 5, "kg", 5.50)
Banan.wyswietl_produkt()
Banan.ile_produktu()
print("{0:.2f}".format(Banan.ile_kosztuje()))


# zadanie 5

class arytm:

    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.an = [self.a1 + (self.r * i) for i in range(self.n)]

    def wyswietl_dane(self):
        print(self.an)

    def pobierz_elementy(self, *an):
        self.an = [x for x in an]

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        self.an = [self.a1 + (self.r * i) for i in range(self.n)]

    def policz_sume(self):
        return sum(self.an)

    def policz_elementy(self):
        return ((self.an[-1] - self.a1) / self.r) + 1


c = arytm(1, 1, 10)
c.wyswietl_dane()

c.pobierz_elementy(1, 3, 5)
c.wyswietl_dane()

c.pobierz_parametry(2, 5, 5)
c.wyswietl_dane()

print(c.policz_sume())
print(c.policz_elementy())


# zadanie 6

class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y = self.y + ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow * self.krok

    def gdzie(self):
        print("x: " + str(self.x))
        print("y: " + str(self.y))


elo = Robaczek(1, 1, 3)
elo.idz_w_lewo(2)
elo.idz_w_prawo(3)
elo.idz_w_dol(5)
elo.idz_w_gore(10)
elo.gdzie()
