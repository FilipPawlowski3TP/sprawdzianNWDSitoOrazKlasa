import math


def nwd(a, b):
    if a == b:
        return a
    if a > b:
        return nwd(a - b, b)
    else:
        return nwd(b - a, a)


print("Najwiekszy wspolny dzielnik to: " + str(nwd(5, 10)))

a = []


def wypelnij(a):
    for i in range(101):
        a.append(True)


wypelnij(a)
n = 100

for i in range(2, int(math.sqrt(n)) + 1):
    if a[i] == True:
        for j in range(2 * i, n + 1, i):
            a[j] = False

print("Liczby pierwsze w zakresie " + str(n) + " To: ")
for i in range(2, n + 1):
    if a[i] == True:
        print(i, end=", ")


class Zadanie:
    idd=0
    def __init__(self, nazwa, punkty):
        self.nazwa = nazwa
        self.punkty = punkty
        self.szkola='Teb wroclaw'
        Zadanie.idd+=1
        self.ile=Zadanie.idd
    def wyswietl(self):
        print(self.nazwa, self.punkty, self.szkola, self.ile)

z1=Zadanie("nwd",20)
z1.wyswietl()