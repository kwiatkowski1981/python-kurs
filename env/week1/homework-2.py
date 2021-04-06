#
# def dziesietna(x):                      # definiujemy funkcje do późniejszego użycia
#     i = len(x) - 1                      # zapisujemy zmienna iteracyjna potrzebna do okreslenia potegi dwojek
#     dec = 0                             # zmienna pomocnicza przechowujaca finalny wynik
#     for c in x:                         # iterujemy poprzez kazda cyfre od lewej
#         dec += int(c) * pow(2, i);      # dodajemy odpowiednia wartosc
#         i -= 1                          # jednoczesnie zmniejszajac wartosc zmiennej iteracyjnej
#     return dec
#
#
# print("Program konwertujacy liczbe binarna na dziesietna")
# a = input("Podaj liczbę binarna a: ")
# print(dziesietna(a))
#
#
# def binarna(x):                         # definiujemy funkcje do późniejszego użycia
#     if x == 0:                          # jezeli liczba jest 0
#         return "0"                      # zwroc od razu wynik
#     b = ""                              # w przeciwnym wypadku tworzymy zmienna pomocnicza przechowujaca liczbe binarna jako tekst
#     while x != 0:                       # dopoki nasza dziesietna liczba nie bedzie rowna 0
#         b = str(x % 2) + b              # dodaj do pomocniczej reszte z dzielenia przez 2
#         x = int(x/2)                    # a nastepnie podziel calkowicie (bez reszty) przez 2
#     return b                            # na koniec zwracamy finalna zmienna
#
#
# print("Program konwertujacy liczbe dziesietna na binarna")
# a = int(input("Podaj liczbę a: "))
# print(binarna(a))

# bin_to_number = input("wpisz cyfre: ")
# number = int(bin_to_number, 2)
# print(number)


# problem z minusem TODO
number_to_bin = int(input("wpisz cyfre: "))
bin_nr = bin(number_to_bin)[2:]
print(f"{bin_nr}")
