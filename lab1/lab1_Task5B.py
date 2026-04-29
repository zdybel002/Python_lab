choosed_month = 10
choosed_year = 2032

def czy_przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    return False

def dni_w_miesiacu(miesiac, rok):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if czy_przestepny(rok):
        dni[1] = 29  # luty = 29 dni
    return dni[miesiac - 1]


wynik = dni_w_miesiacu(choosed_month, choosed_year)

print(f"Miesiąc {choosed_month} w roku {choosed_year} ma {wynik} dni.")


if czy_przestepny(choosed_year):
    print(f"Rok {choosed_year} jest przestępny (luty ma 29 dni).")