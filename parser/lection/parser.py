from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# --- FILTR ANTYSPAMOWY ---
BLACKLIST = [
    "oceń", "dostępna do wypożyczenia", "dostępna w czytelni",
    "brak informacji o dostępności", "Spis treści", "Pokaż więcej ...",
    "Szkoły wyższe", "Książki", "Chcę dowiedzieć się więcej",
    "Dodaj do schowka", "Rezerwuj", "Zamów", "Wyloguj", "Pomoc",
    "Twoje konto", "Historia wyszukiwania", "Schowek", "Koszyk",
    "Poprzednia", "Następna", "Strona główna"
]


def czy_to_ksiazka(tekst):
    tekst = tekst.strip()
    if len(tekst) < 4: return False
    if tekst in BLACKLIST: return False
    if len(tekst) < 15 and tekst[0].isdigit(): return False
    return True


# --- KONFIGURACJA ---
base_url = 'https://biblioteka.pwste.edu.pl/'

print("--- URUCHAMIANIE BOTA V9 (POPRAWIONE ID STRZAŁKI) ---")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(base_url)

print("\n" + "=" * 50)
print(" INSTRUKCJA:")
print(" 1. Wpisz wyszukiwanie i kliknij SZUKAJ.")
print(" 2. Gdy zobaczysz listę, WRÓĆ TUTAJ i wciśnij ENTER.")
print("=" * 50 + "\n")

input("Czekam... Wciśnij ENTER po wyszukaniu książek...")

current_page = 1


total_found = 0
MAX_RECORDS = 100
nazwa_pliku = "wyniki_ksiazki.txt"


uids = set()


plik = open(nazwa_pliku, "w", encoding="utf-8")
plik.write("Autor | Tytuł\n")
plik.write("=" * 50 + "\n")

while True:
    print(f"\n--- Przetwarzam stronę nr {current_page} (Mamy: {total_found}/{MAX_RECORDS}) ---")


    if current_page > 1:
        time.sleep(4)
    else:
        time.sleep(2)

    titles = driver.find_elements(By.CLASS_NAME, "desc-o-mb-title")
    authors = driver.find_elements(By.CLASS_NAME, "desc-o-b-rest")

    nowe_na_tej_stronie = 0

    for t_el, a_el in zip(titles, authors):
        if total_found >= MAX_RECORDS:
            break

        try:
            tytul_surowy = t_el.text.strip()
            autor_surowy = a_el.text.strip()

            tytul = tytul_surowy.strip('" ').strip()
            autor = autor_surowy.lstrip('/ ').strip('" ').strip()

            if tytul:

                unikalne_id = f"{autor}|{tytul}"

                if unikalne_id in uids:
                    continue

                uids.add(unikalne_id)

                print(f"NOWA: {tytul[:40]}...")


                plik.write(f"AUTOR: {autor}\nTYTUŁ: {tytul}\n")
                plik.write("-" * 30 + "\n")

                nowe_na_tej_stronie += 1
                total_found += 1

        except Exception as e:
            continue

    if nowe_na_tej_stronie == 0:
        print("[INFO] Brak nowych książek na tej stronie (może strona się jeszcze ładuje?).")

    # Sprawdzenie limitu
    if total_found >= MAX_RECORDS:
        print(f"\nOsiągnięto limit {MAX_RECORDS} unikalnych książek!")
        break

    # Przejście do następnej strony
    print("Szukam strzałki w prawo...")
    try:

        next_btn = driver.find_element(By.ID, "navi-arr-next")


        driver.execute_script("arguments[0].scrollIntoView();", next_btn)
        time.sleep(1)  # Mała pauza po scrollu

        driver.execute_script("arguments[0].click();", next_btn)

        current_page += 1
        print("-> Kliknięto następna. Czekam na przeładowanie...")

    except Exception as e:
        print(f"Brak przycisku 'Następna' lub błąd: {e}")
        print("Koniec wyników.")
        break

plik.close()
driver.quit()
print(f"\nZakończono. Unikalne dane zapisane w pliku: {nazwa_pliku}")