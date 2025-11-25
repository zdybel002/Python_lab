from datetime import datetime

class Notatka:
    def __init__(self, temat, kategoria, tresc, autor="System"):
        self.temat = temat
        self.kategoria = kategoria
        self.tresc = tresc
        self.autor = autor
        self.data_utworzenia = datetime.now()
        self.data_edycji = self.data_utworzenia
        self.komentarze = []

    def edytuj_tresc(self, nowe_tresc):
        self.tresc = nowe_tresc
        self.data_edycji = datetime.now()

    def __str__(self):
        return (f"[{self.temat} ({self.kategoria})"
                f"Autor: {self.autor}, Utworzono: {self.data_utworzenia}, "
                f"Ostatnia etucja: {self.data_edycji} \n Treść: {self.tresc}")






