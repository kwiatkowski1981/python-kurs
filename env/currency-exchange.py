from sys import exit

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
pln = "PLN"
usd = "USD"


def get_number(prompt="wybierz ilość środków do wymiany: ", err_msg="tylko liczby", parse=int):
    while True:
        try:
            out = parse(input(prompt))
        except ValueError:
            print(err_msg)
        else:
            return out


def ask_for_amount():
    funds_amount = get_number()
    return funds_amount


def sell_usd(funds_amount):
    if funds_amount < 1:
        return print(f"Za mało środków do sprzedaży: {funds_amount}({usd})")
    gained_founds = funds_amount * purchase
    return print(f"za: {funds_amount}({usd}) | otrzymano: {gained_founds:.2f}({pln}).")


def buy_usd(funds_amount):
    gained_founds = funds_amount * sale
    return print(f"Za: {funds_amount}({usd}) | proszę przygotować do zapłaty: {gained_founds:.2f}({pln}).")


def menu_1():
    print(f"Wybrano sprzedaż {usd}")
    sell_usd(ask_for_amount())
    return exit(1)


def menu_2():
    print(f"Wybrano kupno {usd}")
    buy_usd(ask_for_amount())
    return exit(1)


def menu_4():
    return exit(1)


def error():
    print(f"nie ma takiej opcji")
    return exit(1)


def menu_0(argument):
    switcher = {
        1: menu_1,
        2: menu_2,
        3: menu_4,
        # 4: wroc do menu,
    }
    func = switcher.get(argument, lambda: error())
    return func()


def main_menu():
    print("BILONU NIE PRZYJMUJEMY")
    print("Witam w kantorze")
    print("Dostępne opcje to:")
    print(f"1: Sprzedaj {usd}")
    print(f"2: Kup {usd}")
    print("3: Zakończ")
    print("wybierz opcję:")
    menu_0(int(input()))


main_menu()
