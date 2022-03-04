# zadanie 1

s1 = "mekuso\nhanakuso\n"
s2 = "dzieki\ndziala\n"

d1 = 21
d2 = 37

f1 = 4.20
f2 = 10.20

c1 = 2 + 3j
c2 = 3 - 3j

print(s1 + s2)
print(d1, d2, f1, f2, c1, c2)

# zadanie 2

d1 = 21
d2 = 37

dodawanie = d1 + d2
dzielenie = d1 / d2
calkowite = d1 // 2
reszta = d1 % 6
potega = d1 ** 2

print(dodawanie, dzielenie, calkowite, reszta, potega)

# zadanie 3

a = 2
print(a)

a += 2
print(a)

a -= 3
print(a)

a *= 10
print(a)

a /= 5
print(a)

a **= 5
print(a)

a %= 3
print(a)

# zadanie 4

import math

z1 = math.e ** 10
print(z1)

z2 = math.log(5 + (math.sin(8)) ** 2, math.e)
print(z2)

z3 = math.floor(3.55)
print(z3)

z4 = math.ceil(4.80)
print(z4)

# zadanie 5

n = "SEBASTIAN"
s = "MINKOWSKI"
print(n.capitalize() + " " + s.capitalize())

# zadanie 6

la = """la la la la la la la na na na na na
la la na na, la la la la la na na na na na
la la la la la la la na na na na na
la la na na la la la la la na na na na na"""

print(la.count("la"))

# zadanie 7

ebe = "dzieki dziala"
print("druga litera: " + ebe[1] + "\nostatnia litera: " + ebe[-1])

# zadanie 8

import re

la = """la la la la la la ba la na na na na na
la la na na la la la la la ba na na na na na
la la la ba la la la la na na na na na
la la na na la la la ba la la na na na ba na na"""

sp = re.split(" ba |\n", la) # chcialem dwa separatory haha
print(sp)

# zadanie 9

s = "nie no ta\n"
f = 98.652
h = 0xF0

print(s + "jeszcze %(to)f" % {'to': f})
print("albo nawet {0:.3f}".format(f))
print(hex(h))
