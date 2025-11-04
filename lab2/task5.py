# Funkcja rekurencyjna do wyliczania n-tego wyrazu Fibonacciego
def fibonacci_rekur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rekur(n - 1) + fibonacci_rekur(n - 2)

# Pytamy użytkownika o ilość wyrazów
n = int(input("Podaj ile wyrazów ciągu Fibonacciego chcesz wypisać: "))

print("\nWyrazy ciągu Fibonacciego w postaci dwójkowej (rekurencyjnie):")
for i in range(1, n + 1):
    print(bin(fibonacci_rekur(i))[2:])  # [2:] usuwa '0b' z początku
