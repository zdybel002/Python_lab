plik = open("slowa.txt", "r")
tekst = plik.read()
plik.close()

lista_slow = tekst.split()
lista_wynikow = []

for slowo in lista_slow:
    ile_w = 0
    ile_a = 0
    ile_k = 0
    ile_c = 0
    ile_j = 0
    ile_e = 0

    for litera in slowo:
        if litera == 'w':
            ile_w = ile_w + 1
        if litera == 'a':
            ile_a = ile_a + 1
        if litera == 'k':
            ile_k = ile_k + 1
        if litera == 'c':
            ile_c = ile_c + 1
        if litera == 'j':
            ile_j = ile_j + 1
        if litera == 'e':
            ile_e = ile_e + 1

    ile_wakacji = 0

    while True:
        if (ile_w >= 1 and ile_a >= 2 and ile_k >= 1 and
                ile_c >= 1 and ile_j >= 1 and ile_e >= 1):

            ile_wakacji = ile_wakacji + 1
            ile_w = ile_w - 1
            ile_a = ile_a - 2
            ile_k = ile_k - 1
            ile_c = ile_c - 1
            ile_j = ile_j - 1
            ile_e = ile_e - 1
        else:
            break

    lista_wynikow.append(str(ile_wakacji))

plik_wynikowy = open("wyniki2_2.txt", "w")

for wynik in lista_wynikow:
    plik_wynikowy.write(wynik + "\n")

plik_wynikowy.close()

print("Gotowe! Wyniki w pliku wyniki2_2.txt")