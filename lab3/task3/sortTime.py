import time

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # zamiana elementów
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


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
    input_filename = "dane-3.txt"
    output_bubble = "wynik_bubble.txt"
    output_insertion = "wynik_insertion.txt"

    # --- Wczytanie danych z pliku ---
    with open(input_filename, "r") as f:
        data = f.read().split()
        arr = [int(x) for x in data]

    # --- Bubble Sort ---
    arr_bubble = arr.copy()
    start_time = time.time()
    bubble_sorted = bubble_sort(arr_bubble)
    bubble_time = time.time() - start_time

    # Zapis do pliku
    with open(output_bubble, "w") as f:
        f.write("WYNIK BUBBLE SORT\n\n")
        f.write("Posortowane liczby:\n")
        f.write(" ".join(map(str, bubble_sorted)) + "\n\n")
        f.write(f"Czas sortowania: {bubble_time:.6f} sekund\n")

    # --- Insertion Sort ---
    arr_insertion = arr.copy()
    start_time = time.time()
    insertion_sorted = insortSort(arr_insertion)
    insertion_time = time.time() - start_time

    # Zapis do pliku
    with open(output_insertion, "w") as f:
        f.write("WYNIK INSERTION SORT\n\n")
        f.write("Posortowane liczby:\n")
        f.write(" ".join(map(str, insertion_sorted)) + "\n\n")
        f.write(f"Czas sortowania: {insertion_time:.6f} sekund\n")

    # --- Wyniki w konsoli ---
    print("Sortowanie zakończone.")
    print(f"Bubble Sort: {bubble_time:.6f} s (wynik w pliku: {output_bubble})")
    print(f"Insertion Sort: {insertion_time:.6f} s (wynik w pliku: {output_insertion})")


if __name__ == "__main__":
    main()
