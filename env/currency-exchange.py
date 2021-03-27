import sys

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
usd = "Usd"


def ask_for_amount():
    funds_amount = int(input("wybierz ilość środków do wymiany"))
    # print(f"przed retun {funds_amount}")
    return funds_amount


def usd_to_pln(funds_amount):
    gained_founds = funds_amount * sale
    return print(f"{funds_amount}(USD) zamieniono na: {gained_founds}(PLN).")


def pln_to_usd(funds_amount):
    gained_founds = funds_amount * purchase
    return print(f"{funds_amount}(PLN) zamieniono na: {gained_founds}(USD).")


def menu_1():
    print(f"Wybrano wymianę USD na PLN")
    usd_to_pln(ask_for_amount())
    return sys.exit(1)


def menu_2():
    print(f"Wybrano wymianę PLN na USD")
    pln_to_usd(ask_for_amount())
    return sys.exit(1)


def menu_4():
    return sys.exit(1)


def error():
    print(f"nie ma takiej opcji")
    return sys.exit(1)


def menu_0(argument):
    switcher = {
        1: menu_1,
        2: menu_2,
        # 3: wroc do menu,
        4: menu_4,
    }
    func = switcher.get(argument, lambda: error())
    return func()


def main_menu():
    print("Witam w kantorze")
    print("Dostępne opcje to:")
    print(f"1: Wymiana {usd} na {pln}")
    print(f"2: Wymiana {pln} na {usd}")
    print("3: Zakończ")
    print("wybierz opcję:")
    menu_0(int(input()))


main_menu()
