from lab5.task1.Notatka import Notatka


class Komentarz(Notatka):
    def __init__(self, notatka_rodzic, tresc_komentarza):
        temat_komentarza = "Re: " + notatka_rodzic.temat
        super().__init__(temat_komentarza, "Komentarz", tresc_komentarza)
        self.dotyczy_notatki = notatka_rodzic

    def pokaz_info(self):
        print("   [KOMENTARZ]")
        print("   Autor:", self.autor)
        print("   Data:", str(self.data_utworzenia))
        print("   Dotyczy:", self.dotyczy_notatki.temat)
        print("   TREŚĆ:", self.tresc)
        print("")