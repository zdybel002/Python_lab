# Task 5 A

# Varuable of year
choosed_year = 2032


if choosed_year % 400 == 0:
    print("Rok Jest przestepny!")
elif choosed_year % 4 == 0 and choosed_year % 100 != 0:
    print("Rok Jest przestepny!")
else:
    print("Rok nie jest przystepny")