import random

def insortSort(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def main():

    n = int(input("Podaj długość listy: "))
    min_val = int(input("Podaj minimalną wartość liczby: "))
    max_val = int(input("Podaj maksymalną wartość liczby: "))


    lista = [random.randint(min_val, max_val) for _ in range(n)]
    print("\nLista przed sortowaniem:")
    print(lista)


    lista = insortSort(lista)
    print("\nLista po sortowaniu:")
    print(lista)


if __name__ == "__main__":
    main()
