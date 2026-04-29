def main():
    input_filename = "dane-4.txt"
    palindrome_count = 0

    file = open(input_filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        word = line.strip()
        if word == "":
            continue


        if word == word[::-1]:
            palindrome_count += 1

    print("Liczba palindromów w pliku:", palindrome_count)

if __name__ == "__main__":
    main()