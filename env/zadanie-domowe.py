from math import sqrt
# from sympy import Point, Line

# zadanie pierwsze
# celsjusze na faranheity
# wzór ( T(F) = (T(C) * 9/5 +32))

celsius = float(input("podaj temperaturę w stopniach Celsjusza"))
fahrenheits = (celsius * (9 / 5)) + 32
print(f"Po przeliczeniu na Fahrenheit'y temperatura wynosi:{fahrenheits: .2f} stopni \n")

# ****************************************************************************************************************
# ****************************************************************************************************************
# **************************************  zadanie drugie  ********************************************************
# **************************************  oblicz pole trójkąta  **************************************************
# ****************************************************************************************************************
# ****************************************************************************************************************

# dane wejsciowe jako input (wierzcholki)
# a (Xa, Ya)
# b (Xb, Yb)
# c (Xc, Yc)

axis_point = "podaj punkt na osi"
top = "wierzcholka"
#pobieram wierzcholek a:
a_x = int(input(f'{axis_point} x pierwszego {top}'))
a_y = int(input(f'{axis_point} y pierwszego {top} '))
print('\n')
# pobieram wierzcholek b:
b_x = int(input(f'{axis_point} x drugiego {top}'))
b_y = int(input(f'{axis_point} y drugiego {top} '))
print('\n')
# pobieram wierzcholek c:
c_x = int(input(f'{axis_point} x trzeciego {top}'))
c_y = int(input(f'{axis_point} y trzeciego {top} '))
print('\n')

print(f'a_x = {a_x}')
print(f'a_y = {a_y}')

print(f'b_x = {b_x}')
print(f'b_y = {b_y}')

print(f'c_x = {c_x}')
print(f'c_y = {c_y}')

# patern for ab
# https://www.youtube.com/watch?v=HCyeZNotMO4&t=21s

# ab = sqrt(((a_x - b_x) ** 2) + ((a_y - b_y) ** 2))
# print(f'ab = {ab}')
# bc = sqrt(((b_x - c_x) ** 2) + ((b_y - c_y) ** 2))
# print(f'bc = {bc}')
# ca = sqrt(((c_x - a_x) ** 2) + ((c_y - a_y) ** 2))
# print(f'ca = {ca}')


# area_from_heron = (sqrt((distance_a_b + distance_a_c + distance_b_c) * (distance_a_b + distance_a_c - distance_b_c) * (
#         distance_a_b - distance_a_c + distance_b_c) * (- 1 * distance_a_b + distance_a_c + distance_b_c))) / 4
# print(f'Pole powierzchni tego trójkąta: {area_from_heron:.2f}')


# https://eszkola.pl/matematyka/pole-trojkata-w-geometrii-analitycznej-5500.html
#  triangle_areaABC = (1/2) * abs((x_B-x_A)(y_C-y_A)-(y_B-y_A)(x_C-x_A))
triangle_area = 1/2*abs((b_x - a_x) * (c_y - a_y) - (b_y - a_y) * (c_x - a_x))
print(f'pole trojkata o wierzcholkach ({a_x} , {a_y}), ({b_x} , {b_y}), ({c_x} , {c_y}) wynosi {triangle_area}')


# rozwiazanie do przejzenia

# x_a = float(input("Podaj współrzędną x punktu A "))
# y_a = float(input("Podaj współrzędną y punktu A "))
# x_b = float(input("Podaj współrzędną x punktu B "))
# y_b = float(input("Podaj współrzędną y punktu B "))
# x_c = float(input("Podaj współrzędną x punktu C "))
# y_c = float(input("Podaj współrzędną y punktu C "))
#
# p1, p2, p3 = Point(x_a, y_a), Point(x_b, y_b), Point(x_c, y_c)
# l1 = Line(p1, p2)
# point_of_pendicular = list(l1.projection(p3))
# x_h = point_of_pendicular[0]
# y_h = point_of_pendicular[1]
# distance_c_h = sqrt((x_c - x_h) ** 2 + (y_c - y_h) ** 2)
# distance_a_b = sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
# area = 0.5 * distance_c_h * distance_a_b
# print(f'Pole powierzchni tego trójkąta: {area:.2f}')


# ****************************************************************************************************************
# ****************************************************************************************************************
# **************************************  zadanie trzecie  *******************************************************
# **************************************  cyfry 5 i 11 lub obie  *************************************************
# ***************************************  fizzbuzz vers pro :) **************************************************
# ****************************************************************************************************************

number = input("Podaj liczbę całkowitą dowolnego zakresu")

if len(number):
    number = int(number)

    if number % 5 == 0 and number % 11 == 0:
        print(f"Liczba: {number} jest podzielna przez 5 i 11")
    elif number % 5 == 0:
        print(f"Liczba: {number} jest podzielna przez 5")
    elif number % 11 == 0:
        print(f"Liczba: {number} jest podzielna przez 11")
    else:
        print(f"Liczba: {number} nie jest podzielna (bez reszty) ani przez 5 ani przez 11")
else: print('nie podales zadnej liczby \n')

