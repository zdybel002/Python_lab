# Prosta wersja liczenia słów w pliku
def main():

    # Wczytanie danych z pliku
    file = open("dane-4.txt", "r")
    lines = file.readlines()
    file.close()

    words = []
    for line in lines:
        line = line.strip()
        if line != "":
            words.append(line)

    # Liczenie słów
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1

    # Liczenie słów występujących więcej niż raz
    words_more_than_once = 0
    for count in counter.values():
        if count > 1:
            words_more_than_once += 1

    # Szukanie słowa z największą liczbą wystąpień
    most_common_word = ""
    max_count = 0
    for word, count in counter.items():
        if count > max_count:
            max_count = count
            most_common_word = word

    # Wyniki
    print("Liczba słów występujących więcej niż raz:", words_more_than_once)
    print("Słowo o największej liczbie wystąpień:", most_common_word)
    print("Liczba jego wystąpień:", max_count)

if __name__ == "__main__":
    main()
