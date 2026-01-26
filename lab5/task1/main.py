from lab5.task1.Notatnik import Notatnik


moj_notatnik = Notatnik()

moj_notatnik.dodaj_nowa_notatke("Zakupy", "Dom", "Kupić mleko i chleb")
moj_notatnik.dodaj_nowa_notatke("Projekt Python", "Szkoła", "Nauczyć się o klasach")

moj_notatnik.dodaj_komentarz_do_notatki(0, "Aha, jeszcze masło!")

notatka_szkolna = moj_notatnik.lista_wpisow[1]
notatka_szkolna.edytuj_tresc("Nauczyć się o klasach i dziedziczeniu")

moj_notatnik.przegladaj_wszystko()