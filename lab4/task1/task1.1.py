
licznik = 0

with open("pi.txt", "r", encoding="utf-8") as f:
    poprzednia = None

    for linia in f:
        linia = linia.strip()

        if poprzednia is not None:
            polaczone = int(poprzednia + linia)

            if polaczone > 90:
                licznik = licznik + 1

        poprzednia = linia

print("Numbers of ninety is:", licznik)
