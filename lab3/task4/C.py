def main():
    input_filename = "dane-4.txt"
    palindrome_count = 0

    # Otwieramy plik
    file = open(input_filename, "r")
    lines = file.readlines()
    file.close()

    # Sprawdzamy każde słowo
    for line in lines:
        word = line.strip()
        if word == "":
            continue

        # Sprawdzanie palindromu bez odwracania stringa
        is_palindrome = True
        for i in range(len(word)//2):
            if word[i] != word[len(word)-1-i]:
                is_palindrome = False
                break

        if is_palindrome:
            palindrome_count += 1

    # Wyświetlenie wyniku
    print("Liczba palindromów w pliku:", palindrome_count)

if __name__ == "__main__":
    main()
