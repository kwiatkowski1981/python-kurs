numbers = []


def add_numbers():
    the_end = False
    result = 1.0        # todo if result = 1 print "there are no even numbers yet"
    even_numbers = []
    while not the_end:
        number = input("podaj liczbę całkowitą lub wpisz 'end' żeby pomnożyć podane parzyste liczby: ")
        if number != "end":
            numbers.append(float(number))
        else:
            for item in numbers:
                if item % 2 == 0:
                    even_numbers.append(item)
                    result *= float(item)
            the_end = True
            print(f"wynikiem mnożenia podanych liczb jest: {result}")
            print(f"parzyste numery to: {even_numbers}")


add_numbers()
print(f"dodane liczby to:  {numbers}")





