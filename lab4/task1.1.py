# with open("pi.txt", "r", encoding="utf-8") as f:
#     poprzednia = None  # na początku nie ma poprzedniej linii
#
#     for linia in f:
#         linia = linia.strip()
#
#         numberInteration = None
#
#         if numberInteration >
#
#         poprzednia = linia

numberHigterNity = 0

with open("pi.txt", "r", encoding="utf-8") as f:
    poprzednia = None

    for linia in f:
        linia = linia.strip()  # usuń spacje i znaki nowej linii

        if poprzednia is not None:
            polaczone = int(poprzednia + linia)  # konkatenacja jako liczba

            if polaczone > 90:
                numberHigterNity = numberHigterNity + 1

        poprzednia = linia

print("Numbers of ninety is:", numberHigterNity)
