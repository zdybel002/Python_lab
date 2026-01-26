plik = open("pi.txt", "r")
tekst = plik.read()
plik.close()

cyfry = []
for znak in tekst:
    if znak.isdigit():
        cyfry.append(int(znak))

maksymalna_dlugosc = 0
pozycja_startu = 0
znaleziony_ciag = []

for i in range(len(cyfry) - 1):
    dlugosc_rosnaca = 1
    aktualna_pozycja = i

    while aktualna_pozycja > 0:
        if cyfry[aktualna_pozycja] > cyfry[aktualna_pozycja - 1]:
            dlugosc_rosnaca = dlugosc_rosnaca + 1
            aktualna_pozycja = aktualna_pozycja - 1
        else:
            break

    poczatek_ciagu = aktualna_pozycja

    if dlugosc_rosnaca < 2:
        continue

    dlugosc_malejaca = 1
    aktualna_pozycja = i + 1

    while aktualna_pozycja < len(cyfry) - 1:
        if cyfry[aktualna_pozycja] > cyfry[aktualna_pozycja + 1]:
            dlugosc_malejaca = dlugosc_malejaca + 1
            aktualna_pozycja = aktualna_pozycja + 1
        else:
            break

    if dlugosc_malejaca < 2:
        continue

    calkowita_dlugosc = dlugosc_rosnaca + dlugosc_malejaca

    if calkowita_dlugosc > maksymalna_dlugosc:
        maksymalna_dlugosc = calkowita_dlugosc
        pozycja_startu = poczatek_ciagu + 1
        znaleziony_ciag = cyfry[poczatek_ciagu: poczatek_ciagu + calkowita_dlugosc]

print("Zadanie 1.4")
print("Najdłuższy ciąg ma długość:", maksymalna_dlugosc)
print("Zaczyna się na pozycji:", pozycja_startu)
print("Wygląda tak:", znaleziony_ciag)