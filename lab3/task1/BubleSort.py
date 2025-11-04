import random


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


def main():

    # Pobranie danych od użytkownika
    n = int(input("Podaj długość listy: "))
    min_val = int(input("Podaj minimalną wartość liczby: "))
    max_val = int(input("Podaj maksymalną wartość liczby: "))

    # Generowanie listy losowych liczb
    lista = [random.randint(min_val, max_val) for _ in range(n)]
    print("\nLista przed sortowaniem:")
    print(lista)

    # Sortowanie bąbelkowe
    bubble_sort(lista)
    print("\nLista po sortowaniu:")
    print(lista)


# Uruchomienie programu
if __name__ == "__main__":
    main()
