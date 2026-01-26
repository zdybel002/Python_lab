import datetime

AKTUALNY_LOGIN = "JanKowalski"


class Notatka:
    def __init__(self, temat, kategoria, tresc):
        self.temat = temat
        self.kategoria = kategoria
        self.tresc = tresc
        self.autor = AKTUALNY_LOGIN
        teraz = datetime.datetime.now()
        self.data_utworzenia = teraz
        self.data_edycji = teraz

    def edytuj_tresc(self, nowa_tresc):
        self.tresc = nowa_tresc
        self.data_edycji = datetime.datetime.now()
        print("--- Zaktualizowano treść notatki ---")

    def pokaz_info(self):
        print("-" * 30)
        print("Temat:", self.temat)
        print("Kategoria:", self.kategoria)
        print("Autor:", self.autor)
        print("Utworzono:", str(self.data_utworzenia))
        print("Edytowano:", str(self.data_edycji))
        print("TREŚĆ:", self.tresc)
        print("-" * 30)