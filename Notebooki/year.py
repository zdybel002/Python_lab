import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# --- ZMIENNE ---
plik_z_danymi = "cancerPoland.csv"
nazwy_kolumn = ['Rok', 'Wojewodztwo', 'Plec', 'ICD10', 'Wiek', 'Liczba']

# --- 1. Wczytywanie Danych ---
try:
    dane = pd.read_csv(plik_z_danymi, sep=';', encoding='utf-8', on_bad_lines='skip')
    dane.columns = nazwy_kolumn

    dane['Liczba'] = pd.to_numeric(dane['Liczba'], errors='coerce').fillna(0).astype(int)
    dane['Rok'] = pd.to_numeric(dane['Rok'], errors='coerce').fillna(0).astype(int)

except Exception as e:
    print(f"BŁĄD: Nie udało się wczytać pliku: {e}")
    exit()

# --- 2. Przygotowanie Danych do Wykresów ---
trend_roczny = dane.groupby('Rok')['Liczba'].sum().reset_index()

dane_wiekowe = dane.groupby(['Rok', 'Wiek'])['Liczba'].sum().unstack(fill_value=0)
wiek_kolejnosc = sorted(dane_wiekowe.columns.tolist())
dane_wiekowe = dane_wiekowe[wiek_kolejnosc]
lista_lat = dane_wiekowe.index.values

# ----------------------------------------------------
# WYKRES 1: TREND ROCZNY (Wykres Liniowy)
# ----------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(
    trend_roczny['Rok'],
    trend_roczny['Liczba'],
    marker='o',
    color='red'
)

plt.title('TREND ROCZNY: Suma Przypadków w Czasie')
plt.xlabel('Rok')
plt.ylabel('Suma Przypadków')
plt.xticks(trend_roczny['Rok'].unique())
plt.grid(True)
plt.tight_layout()
plt.show()
plt.close()

# ----------------------------------------------------
# WYKRES 2: SKUMULOWANY SŁUPKOWY (Rok vs. Wiek)
# ----------------------------------------------------

plt.figure(figsize=(10, 6))

podstawa = np.zeros(len(lista_lat))
ile_grup = len(wiek_kolejnosc)
kolory_mapa = plt.colormaps['hsv']
norma_koloru = plt.Normalize(vmin=0, vmax=ile_grup - 1)

for i, grupa_wiekowa in enumerate(wiek_kolejnosc):
    ilosc = dane_wiekowe[grupa_wiekowa].values
    kolor_dla_grupy = kolory_mapa(norma_koloru(i))

    plt.bar(
        lista_lat,
        ilosc,
        bottom=podstawa,
        label=grupa_wiekowa,
        color=kolor_dla_grupy
    )
    podstawa += ilosc

plt.title('SKUMULOWANY WYKRES: Podział na Wiek')
plt.xlabel('Rok')
plt.ylabel('Suma Przypadków')
plt.legend(title='Wiek', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(lista_lat)

plt.tight_layout()
plt.show()
plt.close()

# --- PODSUMOWANIE ---
print("\n--- Wykonano ---")
print("Wyświetlono dwa wykresy.")