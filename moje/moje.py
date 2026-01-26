import pandas as pd

def main():
    # wczytanie pliku
    df = pd.read_excel("dane.xlsx")

    # filtr semestr 2
    df["SEMESTER"] = df["SEMESTER"].astype(str).str.strip()
    filtered = df[df["SEMESTER"] == "2"]

    # usunięcie pustych kolumn
    filtered = filtered.dropna(axis=1, how='all')

    # zapis do nowego pliku
    filtered.to_excel("wynik_semester_2.xlsx", index=False)

    print(f"Liczba wierszy: {len(filtered)}, liczba kolumn: {len(filtered.columns)}")
    print("Plik wynik_semester_2.xlsx został zapisany.")

if __name__ == "__main__":
    main()
