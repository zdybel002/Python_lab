# Tworzymy listę studentów
studenci = ["Kasia", "Basia", "Marek", "Darek"]

# Dodajemy Józka do listy
studenci.append("Józek")

# Dodajemy Anię i Basię do listy
studenci.extend(["Ania", "Basia"])

# Sortujemy listę alfabetycznie
studenci.sort()

# Wypisujemy czwartego studenta
print("Czwarty student:", studenci[3])

# Wypisujemy dwóch pierwszych studentów
print("Dwóch pierwszych studentów:", studenci[0:2])

# Wypisujemy dwóch ostatnich studentów
print("Dwóch ostatnich studentów:", studenci[-2:])

# Usuwamy wszystkie Basie
while "Basia" in studenci:
    studenci.remove("Basia")

# Sprawdzamy ilość studentów
print("Liczba studentów:", len(studenci))

# Wypisujemy finalną listę studentów
print("Lista studentów:", studenci)
