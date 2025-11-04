# Funkcja iteracyjna do wyliczania n-tego wyrazu Fibonacciego
def fibonacci_iter(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    return b

# Funkcja rekurencyjna do wyliczania n-tego wyrazu Fibonacciego
def fibonacci_rekur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rekur(n - 1) + fibonacci_rekur(n - 2)

# Pytamy użytkownika o numer wyrazu
n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))

# Wyliczamy i wypisujemy wynik iteracyjnie
print("Wyraz", n, "ciągu Fibonacciego (iteracyjnie):", fibonacci_iter(n))

# Wyliczamy i wypisujemy wynik rekurencyjnie
print("Wyraz", n, "ciągu Fibonacciego (rekurencyjnie):", fibonacci_rekur(n))
