
def najczestszy_fragment(array):
    if len(array) == 0:
        return None

    max_wystapien = 0
    najczestszy = None

    for para, liczba in array:
        if liczba > max_wystapien:
            max_wystapien = liczba
            najczestszy = para

    return najczestszy, max_wystapien


def najrzadszy_fragment(array):
    if not array:
        return None


    najrzadszy, min_wystapien = array[0]

    for para, liczba in array:
        if liczba < min_wystapien:
            min_wystapien = liczba
            najrzadszy = para

    return najrzadszy, min_wystapien



array = []

with open("pi.txt", "r", encoding="utf-8") as f:
    text = ""
    for linia in f:
        text += linia.strip()


for i in range(10):
    for j in range(10):
        para = str(i) + str(j)
        liczba_powtorzen = text.count(para)
        array.append((para, liczba_powtorzen))


print("\nWszystkie wyniki:")
print(array)

najczestsze, na_ile = najczestszy_fragment(array)
najrzadszy_fragment, ile = najrzadszy_fragment(array)

print("Najczęstsze fragmenty:", najczestsze)
print("Liczba wystąpień:", na_ile)

print("Najczęstsze fragmenty:", najrzadszy_fragment)
print("Liczba wystąpień:", ile)


















