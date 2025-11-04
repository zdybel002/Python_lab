# Task 5 A

# Varuable of year
choosed_day = 21
choosed_mouth = 10
choosed_year = 2032




# Funkcja sprawdzająca czy rok jest przestępny
def czy_przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    else:
        return False


# Funkcja zwracająca liczbę dni w miesiącach
def dni_w_miesiacu(miesiac, rok):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if czy_przestepny(rok):
        dni[1] = 29  # luty = 29 dni
    return dni[miesiac - 1]