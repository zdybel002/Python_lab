# Tworzymy listę wszystkich wielokrotności 3 mniejszych od 100
lista = list(range(3, 100, 3))
print("Lista wielokrotności 3:", lista)

# Usuwamy co trzeci element, zaczynając od piątego
del lista[4::3]
print("Lista po usunięciu co trzeciego elementu od piątego:", lista)

# Sprawdzamy definicję funkcji sum
help(sum) #opis funkcji w konsoli Pythona

# Liczymy średnią arytmetyczną
srednia = sum(lista) / len(lista)
print("Średnia arytmetyczna:", srednia)
