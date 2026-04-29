import requests
from bs4 import BeautifulSoup

# Adres URL, z którego chcesz pobrać dane
url = 'https://doci.pl/korazowsky/pdf-1+dvmnn88'

# Nagłówki udające prawdziwą przeglądarkę (ważne, aby strona nie zablokowała skryptu)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 1. Pobranie strony
    response = requests.get(url, headers=headers)

    # Sprawdzenie, czy pobieranie się udałow (kod 200 = OK)
    if response.status_code == 200:
        # 2. Przetworzenie HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Lista na znalezione tytuły
        titles = []

        # 3. Szukanie elementów na podstawie Twojego zrzutu ekranu
        # Szukamy divów z klasą "text-ellipsis elipsis-file"
        file_divs = soup.find_all('div', class_='text-ellipsis elipsis-file')

        for div in file_divs:
            link = div.find('a')
            if link:
                # Pobranie tekstu i usunięcie zbędnych spacji
                title = link.get_text().strip()
                if title:  # Dodaj tylko jeśli tytuł nie jest pusty
                    titles.append(title)

        # 4. Wyświetlenie wyników
        print(f"Znaleziono {len(titles)} plików:")
        print("-" * 30)
        for t in titles:
            print(t)

    else:
        print(f"Błąd pobierania strony. Kod błędu: {response.status_code}")

except Exception as e:
    print(f"Wystąpił błąd: {e}")