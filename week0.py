from math import sqrt

print(2 * 17)

a = 66
b = 5
c = a % b
d = a // b
print(c)
print(d)

print(9 ** 3)

print(int(123321 / 11))  # konwersja jawna typu z float na int (pozbywam sie wartosci po przecinku)

print(sqrt(121))  # import  z biblioteki ==>>>  from math import sqrt

print(27 ** (1 / 3))  # inna forma zapisu wyciągania pierwiastków BEZ importowania z biblioteki funkcji SQRT
print(9 ** (1 / 2))  # tak samo jak wyej tylko przyklad do potegi drugiej a nie trzeciej

print(type(123321 / 11))  # sprawdzam typ wyniku wyrazenia

route = 150
fuelPrice = 5
fuelUsage = 6

fuelConsumption = (route * fuelUsage) / 100
fuelCost = fuelConsumption * fuelPrice
print(f'zuzycie paliwa na trasie {route}km to {int(fuelConsumption)} litrów i kosztuje nas to {int(fuelCost)}$')

first = 3.14
second = 3, 14
print(type(first))
print(type(second))

