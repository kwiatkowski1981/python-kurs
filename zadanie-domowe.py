# zadanie pierwsze
# celsjusze na faranheity
# wzór ( T(F) = (T(C) * 9/5 +32))

# celsius = float(input("podaj temperaturę w stopniach Celsjusza"))
# fahrenheits = (celsius * (9 / 5)) + 32
# print(f"Po przeliczeniu na Fahrenheit'y temperatura wynosi:{fahrenheits: .2f} stopni \n")

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
# pobieram wierzcholek a:
a_x = int(input('podaj punkt na osi x pierwszego wierzcholka'))
a_y = int(input('podaj punkt na osi y pierwszego wierzcholka '))
print('\n')
# pobieram wierzcholek b:
b_x = int(input('podaj punkt na osi x drugiego wierzcholka'))
b_y = int(input('podaj punkt na osi y drugiego wierzcholka '))
print('\n')
# pobieram wierzcholek c:
c_x = int(input('podaj punkt na osi x trzeciego wierzcholka'))
c_y = int(input('podaj punkt na osi y trzeciego wierzcholka '))
print('\n')

# # wzor na pole trojkata przy znanych wierzcholkach
# # https://szaloneliczby.pl/pole-trojkata-abc-o-wierzcholkach-a-0-0-b-4-2-c-2-6-jest-rowne/
# # p1 = (1/2) * (Ya + Yc) * (Ya + Xc)
# # p2 = (1/2) * (Xa + Xb) * (Xb + Yb)
# # p3 = (1/2) * ((a_y + c_y) - (a_y + b_y)) * ((a_x + b_x) - (a_y + c_x))
# # wyliczam pola trójkątów dookoła trójkąta głównego
# triangle_area_1 = (1/2) * (a_y + c_y) * (a_y + c_x)
# print(f'pole trojkata 1 to {triangle_area_1}')
# triangle_area_2 = (1/2) * (a_x + b_x) * (a_y + b_y)
# print(f'pole trojkata 2 to {triangle_area_2}')
# triangle_area_3 = (1/2) * ((a_y + c_y) - (a_y + b_y)) * ((a_x + b_x) - (a_y + c_x))
# # print((b_y + c_y) - (a_x + b_y))
# print(f'pole trojkata 3 to {triangle_area_3}')
# # pole prostokatu, w ktorym jest trojkat
# # rectangle_area = (a_x + c_y) * (a_y + b_x)
# rectangle_area = (a_x + c_y) * (a_y + b_x)
# print(f'pole prostokatu to {rectangle_area}')
# # suma pól trójkątów bocznych
# # triangle_area_123 = p1 + p2 + p3
# triangle_area_123 = triangle_area_1 + triangle_area_2 + triangle_area_3
# print(f'suma pol wszystkich trojkatow to {triangle_area_123}')
# # pole trójkąta właściwego
# # p(abc) = rectangle_area - triangle_area_123
# main_triangle_area = rectangle_area - triangle_area_123
# print(f"Pole trójkąta o wierzchołkach ({a_x} , {a_y}), ({b_x} , {b_y}), ({c_x} , {c_y}) wynosi {main_triangle_area}")

# ****************************************************************************************************************
# ****************************************************************************************************************
# **************************************  zadanie trzecie  *******************************************************
# **************************************  cyfry 5 i 11 lub obie  *************************************************
# ***************************************  fizzbuzz vers pro :) **************************************************
# ****************************************************************************************************************

# number = input("Podaj liczbę całkowitą dowolnego zakresu")
#
# if len(number):
#     number = int(number)
#
#     if number % 5 == 0 and number % 11 == 0:
#         print(f"Liczba: {number} jest podzielna przez 5 i 11")
#     elif number % 5 == 0:
#         print(f"Liczba: {number} jest podzielna przez 5")
#     elif number % 11 == 0:
#         print(f"Liczba: {number} jest podzielna przez 11")
#     else:
#         print(f"Liczba: {number} nie jest podzielna (bez reszty) ani przez 5 ani przez 11")
# else: print('nie podales zadnej liczby \n')

