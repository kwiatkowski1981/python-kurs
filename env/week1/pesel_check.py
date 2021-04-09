pesel = input("Podaj pesel: ")
pesel_list = list(pesel)
list_q = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
suma = 0
for pes, quan in zip(pesel, list_q):
    suma += int(pes) * quan
print(suma)
print(f"Pesel {pesel} jest poprawny") if suma % 10 == 0 else print(f"Pesel {pesel} nie jest prawidłowy")
# 81042108198
