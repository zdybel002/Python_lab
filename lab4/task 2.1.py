plik_wejsciowy = open("slowa.txt", "r")
plik_wynikowy = open("wyniki2_1.txt", "w")

tresc = plik_wejsciowy.read()
lista_slow = tresc.split()

for slowo in lista_slow:
    liczba_w = 0
    liczba_k = 0

    for litera in slowo:
        if litera == 'w':
            liczba_w = liczba_w + 1
        if litera == 'k':
            liczba_k = liczba_k + 1

    if liczba_w == liczba_k:
        plik_wynikowy.write(slowo + "\n")

plik_wejsciowy.close()
plik_wynikowy.close()

print("Gotowe! Wyniki zapisano w pliku wyniki2_1.txt")