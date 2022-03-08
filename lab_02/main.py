# zadanie 1

sport = ["hockey", "volleyball", "rugby"]
sport.reverse()
sport.append("baseball")
sport.append("football")

# zadanie 2

short = {"np.": "na przykład", "tzn.": "to znaczy", "str.": "strona"}

# zadanie 3

games = {1: "Path of Exile", 2: "Tetris The Grandmaster 3", 3: "Final Fantasy XIV"}
print(len(games))

# zadanie 4

a = input("Napisz zdanie: ")
print("Napisane zdanie posiada " + str(len(a)) + " znaków.")

# zadanie 5

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = (a ** b) + c

sys.stdout.write(str(result))

# zadanie 6

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a > b:
    if a > c:
        print("a jest najwieksza")
    elif a < c:
        print("c jest najwieksza")
    else:
        print("a i c sa rowne i najwieksze")
elif b > a:
    if b > c:
        print("b jest najwieksza")
    elif b < c:
        print("c jest najwieksza")
    else:
        print("b i c sa rowne i najwieksze")
elif a == b:
    if a == c:
        print("wszystkie liczby sa rowne")
    elif a > c:
        print("a i b sa rowne i najwieksze")
    elif a < c:
        print('c jest najwieksza')

# zadanie 7

numbers = [1, 6.2, 420, 360, 5.75]
i = 0

for n in numbers:
    numbers[i] = n ** 2
    i += 1

print(numbers)

# zadanie 8

list = []
n = 0

while n < 10:
    x = float(input())
    if x % 2 == 0:
        list.append(x)
    n += 1

print(list)

# zadanie 9

import math

try:
    n = float(input("Podaj liczbe do pierwiastkowania: "))
    n = math.sqrt(n)
    print(n)
except ValueError:
    print("ValueError - podano liczbe ujemna.")
