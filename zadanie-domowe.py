# zadanie pierwsze
# celsjusze na faranheity
# wzór ( T(F) = (T(C) * 9/5 +32))

celsius = float(input("podaj temperaturę w stopniach Celsjuszach"))
fahrenheits = (celsius * (9/5)) + 32
print(f"Po przeliczeniu na Fahrenheit'y temperatura wynosi:{fahrenheits: .2f} stopni \n")


# zadanie drugie
# oblicz pole trójkąta


# zadanie trzecie
# fizzbuzz vers pro :)
# cyfry 5 i 11 lub obie

number = int(input("Podaj liczbę całkowitą dowolnego zakresu"))

if number % 5 == 0 and number % 11 == 0:
    print(f"Liczba: {number} jest podzielna przez 5 i 11")
elif number % 5 == 0:
    print(f"Liczba: {number} jest podzielna przez 5")
elif number % 11 == 0:
    print(f"Liczba: {number} jest podzielna przez 11")
else:
    print(f"Liczba: {number} nie jest podzielna (bez reszty) ani przez 5 ani przez 11")
