plik = open("pi.txt", "r")
tekst = plik.read()
plik.close()

cyfry = []
for znak in tekst:
    if znak.isdigit():
        cyfry.append(int(znak))

licznik = 0
dlugosc_ciagu = 6

for i in range(len(cyfry) - dlugosc_ciagu + 1):
    a = cyfry[i: i + 6]
    czy_jest_dobry = False

    if (a[0] < a[1]) and (a[2] > a[3] and a[3] > a[4] and a[4] > a[5]):
        czy_jest_dobry = True

    if (a[0] < a[1] and a[1] < a[2]) and (a[3] > a[4] and a[4] > a[5]):
        czy_jest_dobry = True

    if (a[0] < a[1] and a[1] < a[2] and a[2] < a[3]) and (a[4] > a[5]):
        czy_jest_dobry = True

    if czy_jest_dobry:
        licznik = licznik + 1

print("Liczba ciągów rosnąco-malejących:", licznik)