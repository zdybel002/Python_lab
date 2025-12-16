import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Hej! Tutaj ustawiamy styl wykresów, żeby ładnie wyglądały
plt.style.use('ggplot')

# --- Ustawienia Pliku ---
plik_z_danymi = "cancerPoland.csv"  # Nazwa Twojego pliku!
# Jakie kolumny mamy w pliku:
nazwy_kolumn = ['Rok', 'Wojewodztwo', 'Plec', 'ICD10', 'Wiek', 'Liczba']


# --- 1. Wczytywanie Danych ---
print("Zaczynam wczytywać dane...")
try:
    # Wczytanie pliku CSV, pamiętamy o średniku (sep=';')
    dane = pd.read_csv(plik_z_danymi, sep=';', encoding='utf-8', on_bad_lines='skip')
    dane.columns = nazwy_kolumn  # Ustawiamy polskie nazwy kolumn

    # Czyszczenie i zamiana na liczby, żeby Pandas nas słuchał
    dane['Liczba'] = pd.to_numeric(dane['Liczba'], errors='coerce').fillna(0).astype(int)
    dane['Rok'] = pd.to_numeric(dane['Rok'], errors='coerce').fillna(0).astype(int)

except Exception as e:
    print(f"Ups! Coś poszło nie tak przy wczytywaniu pliku: {e}")
    # Jeśli tu jesteś, to pewnie plik cancerPoland.csv nie jest obok skryptu!
    exit()

# --- 2. Przygotowanie Danych do Wykresów ---

# A) TREND ROCZNY (Potrzebujemy sumy przypadków na każdy rok)
trend_roczny = dane.groupby('Rok')['Liczba'].sum().reset_index()

# B) DANE WIEKOWE (Potrzebujemy danych Rok po Roku i Wiek po Wieku)
dane_wiekowe = dane.groupby(['Rok', 'Wiek'])['Liczba'].sum().unstack(fill_value=0)
wiek_kolejnosc = sorted(dane_wiekowe.columns.tolist())
dane_wiekowe = dane_wiekowe[wiek_kolejnosc]
lista_lat = dane_wiekowe.index.values

print("Dane gotowe! Teraz robimy wykresy...")

# ----------------------------------------------------
# WYKRES 1: TREND ROCZNY (Wykres Liniowy)
# ----------------------------------------------------

plt.figure(figsize=(8, 5))  # Mały, ładny obrazek
plt.plot(
    trend_roczny['Rok'],
    trend_roczny['Liczba'],
    marker='o',
    color='red'  # Używamy prostego koloru
)

plt.title('TREND ROCZNY: Ile było wszystkich przypadków w danym roku?')
plt.xlabel('Rok')
plt.ylabel('Suma Przypadków')
plt.xticks(trend_roczny['Rok'].unique())  # Proste znaczniki lat
plt.grid(True)
plt.tight_layout()
plt.show()  # Pokaż!
plt.close()

# ----------------------------------------------------
# WYKRES 2: SKUMULOWANY SŁUPKOWY (Rok vs. Wiek)
# ----------------------------------------------------

plt.figure(figsize=(10, 6))

podstawa = np.zeros(len(lista_lat))
ile_grup = len(wiek_kolejnosc)

# Używamy Matplotlib do wybrania unikalnych kolorów
kolory_mapa = plt.colormaps['hsv']
norma_koloru = plt.Normalize(vmin=0, vmax=ile_grup - 1)

# Pętla przez każdą grupę wiekową
for i, grupa_wiekowa in enumerate(wiek_kolejnosc):
    ilosc = dane_wiekowe[grupa_wiekowa].values

    # Wybieramy unikalny kolor dla tej grupy
    kolor_dla_grupy = kolory_mapa(norma_koloru(i))

    plt.bar(
        lista_lat,
        ilosc,
        bottom=podstawa,  # Ważne: budujemy słupki na sobie!
        label=grupa_wiekowa,
        color=kolor_dla_grupy
    )
    podstawa += ilosc  # Zwiększamy wysokość podstawy

plt.title('SKUMULOWANY WYKRES: Podział na Wiek (każdy Wiek to inny kolor)')
plt.xlabel('Rok')
plt.ylabel('Suma Przypadków')
# Legenda obok, żeby nie zasłaniała wykresu
plt.legend(title='Wiek', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(lista_lat)

plt.tight_layout()
plt.show()  # Pokaż!
plt.close()

# --- PODSUMOWANIE ---
print("\n--- Zrobione! ---")
print("Powinny pojawić się dwa wykresy. Fajnie, co nie?")