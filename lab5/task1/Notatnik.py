import os
from lab5.task1.Komentarz import Komentarz
from lab5.task1.Notatka import Notatka


class Notatnik:
    def __init__(self):
        self.lista_wpisow = []

    def dodaj_nowa_notatke(self, temat, kategoria, tresc):
        nowa = Notatka(temat, kategoria, tresc)
        self.lista_wpisow.append(nowa)
        print("Dodano notatkę:", temat)

    def dodaj_komentarz_do_notatki(self, numer_notatki, tresc_komentarza):
        if numer_notatki < len(self.lista_wpisow):
            notatka_rodzic = self.lista_wpisow[numer_notatki]

            if isinstance(notatka_rodzic, Notatka):
                nowy_komentarz = Komentarz(notatka_rodzic, tresc_komentarza)
                self.lista_wpisow.append(nowy_komentarz)
                print("Dodano komentarz do notatki:", notatka_rodzic.temat)
            else:
                print("To nie jest notatka!")
        else:
            print("Nie ma notatki o takim numerze.")

    def przegladaj_wszystko(self):
        print("\n=== ZAWARTOŚĆ NOTATNIKA ===")
        numer = 0
        for wpis in self.lista_wpisow:
            print("Nr indeksu:", numer)
            wpis.pokaz_info()
            numer = numer + 1

    def usun_wpis(self, numer):
        if numer < len(self.lista_wpisow):
            usuniety = self.lista_wpisow.pop(numer)
            print("Usunięto:", usuniety.temat)
        else:
            print("Błąd: zły numer.")

    def zapisz_do_pliku(self):
        plik = open("baza_notatek.txt", "w", encoding="utf-8")
        for wpis in self.lista_wpisow:
            if isinstance(wpis, Komentarz):
                plik.write("KOMENTARZ\n")
                plik.write(wpis.temat + "\n")
                plik.write(wpis.kategoria + "\n")
                plik.write(wpis.tresc.replace("\n", " ") + "\n")
                plik.write(wpis.autor + "\n")
                # Tu byla poprawka - dodano str()
                plik.write(str(wpis.data_utworzenia) + "\n")
                plik.write(str(wpis.data_edycji) + "\n")
                plik.write(wpis.dotyczy_notatki.temat + "\n")
            else:
                plik.write("NOTATKA\n")
                plik.write(wpis.temat + "\n")
                plik.write(wpis.kategoria + "\n")
                plik.write(wpis.tresc.replace("\n", " ") + "\n")
                plik.write(wpis.autor + "\n")
                # Tu byla poprawka - dodano str()
                plik.write(str(wpis.data_utworzenia) + "\n")
                plik.write(str(wpis.data_edycji) + "\n")
            plik.write("###\n")
        plik.close()
        print("Zapisano dane do pliku.")

    def wczytaj_z_pliku(self):
        if not os.path.exists("baza_notatek.txt"):
            return

        plik = open("baza_notatek.txt", "r", encoding="utf-8")
        tresc = plik.read()
        plik.close()

        wpisy = tresc.split("###\n")
        for kawalek in wpisy:
            linie = kawalek.strip().split("\n")
            if len(linie) < 6:
                continue

            typ = linie[0]
            temat = linie[1]
            kategoria = linie[2]
            tresc_notatki = linie[3]
            autor = linie[4]
            data_utw = linie[5]
            data_ed = linie[6]

            if typ == "NOTATKA":
                obj = Notatka(temat, kategoria, tresc_notatki)
                obj.autor = autor
                obj.data_utworzenia = data_utw
                obj.data_edycji = data_ed
                self.lista_wpisow.append(obj)

            elif typ == "KOMENTARZ":
                temat_rodzica = linie[7]
                dummy_rodzic = Notatka(temat_rodzica, "", "")
                obj = Komentarz(dummy_rodzic, tresc_notatki)
                obj.temat = temat
                obj.kategoria = kategoria
                obj.autor = autor
                obj.data_utworzenia = data_utw
                obj.data_edycji = data_ed
                self.lista_wpisow.append(obj)
        print("Wczytano dane z pliku.")