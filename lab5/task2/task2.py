from lab5.task1.Notatnik import Notatnik

aplikacja = Notatnik()
aplikacja.wczytaj_z_pliku()

while True:
    print("\n--- MENU ---")
    print("1. Dodaj notatke")
    print("2. Dodaj komentarz")
    print("3. Przegladaj notatnik")
    print("4. Usun wpis")
    print("5. Edytuj wpis")
    print("0. Zapisz i wyjdz")

    wybor = input("Wybierz opcje: ")

    if wybor == "1":
        t = input("Podaj temat: ")
        k = input("Podaj kategorie: ")
        tr = input("Podaj tresc: ")
        aplikacja.dodaj_nowa_notatke(t, k, tr)

    elif wybor == "2":
        aplikacja.przegladaj_wszystko()
        try:
            nr = int(input("Podaj ID notatki do skomentowania: "))
            tr = input("Podaj tresc komentarza: ")
            aplikacja.dodaj_komentarz_do_notatki(nr, tr)
        except ValueError:
            print("To nie jest liczba")

    elif wybor == "3":
        aplikacja.przegladaj_wszystko()

    elif wybor == "4":
        try:
            nr = int(input("Podaj ID do usuniecia: "))
            aplikacja.usun_wpis(nr)
        except ValueError:
            print("To nie jest liczba")

    elif wybor == "5":
        try:
            nr = int(input("Podaj ID do edycji: "))
            if nr < len(aplikacja.lista_wpisow):
                nowa = input("Podaj nowa tresc: ")
                aplikacja.lista_wpisow[nr].edytuj_tresc(nowa)
            else:
                print("Nie ma takiego ID")
        except ValueError:
            print("To nie jest liczba")

    elif wybor == "0":
        aplikacja.zapisz_do_pliku()
        break

    else:
        print("Nieznana opcja")