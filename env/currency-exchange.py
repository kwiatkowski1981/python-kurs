# Prepare two variables, containing the buying rate and the USD selling rate. As of today,
# this is the purchase of 3.8507, the sale of 3.9285.
# Your task will be to ask the user what he wants to buy / sell, then ask him for
# the amount of zlotys or dollars to be exchanged, and then inform what value the user will receive after the exchange.


# Przygotuj dwie zmienne, zawierające kurs kupna oraz kurs sprzedaży USD.
# Na dzień dzisiejszy to kupno 3.8507, sprzedaż 3,9285.
# Twoim zadaniem będzie zapytać użytkownika o to co chce zrobić kupić/sprzedać,
# następnie zapytać go o ilość złotówek lub dolarów do wymiany,
# a następnie poinformować jaką wartość po wymianie użytkownik otrzyma.

purchase = 3.8507
sale = 3.9285
pln = "Pln"
usd = " Usd"
funds_amount_text = "enter the amount of funds to be exchanged"
funds_amount = 0


def usd_to_pln():
    gained_founds = funds_amount * sale
    return gained_founds


def pln_to_usd():
    gained_founds = funds_amount * purchase
    return gained_founds


def menu(argument):
    switcher = {
        "1": "Wymianę USD na Pln",
        "2": "Wymianę Pln na USD",
    }
    print(f"Wybrał/a pan/i {switcher.get(argument, 'zły numer')}")


menu(input("prosze wybrac opcje menu"))
