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
    if len(tekst) < 4: return False  # Za krótkie (np. "1", "2")
    if tekst in BLACKLIST: return False
    # Ignoruj sygnatury (zaczynają się od cyfr/liter, są krótkie)
    if len(tekst) < 15 and tekst[0].isdigit(): return False
    return True


# --- KONFIGURACJA ---
base_url = 'https://biblioteka.pwste.edu.pl/'

print("--- URUCHAMIANIE BOTA V7 (ODKURZACZ) ---")
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
uids = set()  # Zbiór unikalnych książek, żeby nie wypisywać duplikatów

while True:
    print(f"\n--- Przetwarzam stronę nr {current_page} ---")
    time.sleep(2)

    # 1. POBIERANIE WSZYSTKICH LINKÓW I NAGŁÓWKÓW
    # Bierzemy wszystko co jest linkiem (a) lub nagłówkiem (h3)
    elements = driver.find_elements(By.TAG_NAME, "a")

    znaleziono_na_stronie = 0

    for el in elements:
        try:
            txt = el.text.strip()

            # FILTRACJA
            if not czy_to_ksiazka(txt):
                continue

            # Jeśli już to widzieliśmy na tej stronie (duplikaty w kodzie), pomiń
            if txt in uids:
                continue

            # LOGIKA ROZDZIELANIA TYTUŁU
            if "/" in txt:
                parts = txt.split("/", 1)
                tytul = parts[0].strip()
                autor = parts[1].strip()
                # Dodatkowy filtr: autor nie może być pusty
                if len(autor) < 2: continue
            else:
                # Jeśli tekst jest bardzo długi, to pewnie tytuł bez autora w tej linii
                if len(txt) > 20:
                    tytul = txt
                    autor = "--- (brak ukośnika w linku)"
                else:
                    continue  # Za krótkie na tytuł bez autora

            print(f"KSIĄŻKA: {tytul}")
            print(f"  AUTOR: {autor}")
            print("-" * 30)

            uids.add(txt)  # Zapamiętujemy, żeby nie dublować
            znaleziono_na_stronie += 1

        except:
            continue

    # Czyścimy pamięć duplikatów co stronę, żeby na nowej stronie znów zbierać
    uids.clear()

    if znaleziono_na_stronie == 0:
        print("[ALARM] Bot nie widzi książek. Czy lista na pewno się załadowała?")
        # Opcja debugowania - odkomentuj poniżej, żeby zobaczyć co bot widzi
        # print("DEBUG - Przykładowe teksty, które widzę:")
        # for e in elements[:10]: print(f" -> '{e.text}'")

    # 2. KLIKANIE STRZAŁKI "NASTĘPNA"
    print("Szukam strzałki w prawo...")
    try:
        # Metoda ID (potwierdzona przez Ciebie)
        next_btn = driver.find_element(By.ID, "navi-arr-ix-next")

        # Scroll i Klik
        driver.execute_script("arguments[0].scrollIntoView();", next_btn)
        driver.execute_script("arguments[0].click();", next_btn)

        current_page += 1
        print("-> Przechodzę dalej...")
        time.sleep(4)

    except:
        print("Brak przycisku 'Następna'. Koniec wyników.")
        break

print("\nZakończono.")


