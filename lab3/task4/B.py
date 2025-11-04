def main():
    input_filename = "dane-4.txt"
    even_count = 0

    file = open(input_filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        number = int(line, 16)
        if number % 2 == 0:
            even_count += 1

    print("Liczb parzystych w pliku:", even_count)

if __name__ == "__main__":
    main()
