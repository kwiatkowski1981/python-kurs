pesel = input("podaj pesel do sprawdzenia: ")
# pesel = str(81042108198)

# pesel_check_pattern = (1*a + 3*b + 7*c + 9*d + 1*e + 3*f + 7*g + 9*h + 1*i + 3*j)
# check_number = 10 - pesel_check_pattern[-1:]
# if pesel[-1:] == check_number? True = ok else False =  not ok

pesel_to_list = list(pesel)
# print(pesel_to_list)
pesel_check_pattern_part_one = (int(pesel_to_list[0]) * 1) + (int(pesel_to_list[1]) * 3) + (int(pesel_to_list[2]) * 7)\
                      + (int(pesel_to_list[3]) * 9) + (int(pesel_to_list[4]) * 1) + (int(pesel_to_list[5]) * 3)\
                      + (int(pesel_to_list[6]) * 7) + (int(pesel_to_list[7]) * 9) + (int(pesel_to_list[8]) * 1)\
                      + (int(pesel_to_list[9]) * 3)


print(int(pesel_to_list[0]) * 1)
print(int(pesel_to_list[1]) * 3)
print(int(pesel_to_list[2]) * 7)
print(int(pesel_to_list[3]) * 9)
print(int(pesel_to_list[4]) * 1)
print(int(pesel_to_list[5]) * 3)
print(int(pesel_to_list[6]) * 7)
print(int(pesel_to_list[7]) * 9)
print(int(pesel_to_list[8]) * 1)
print(int(pesel_to_list[9]) * 3)
print(f"suma mnożenia ze wzoru na poprawny pesel: {pesel_check_pattern_part_one}")
print(type(pesel_check_pattern_part_one))

last_pesel_number_str = str(pesel_check_pattern_part_one)
print(f"ostatnia cyfra ze wzoru: {last_pesel_number_str[-1:]}")
print(f"ostatnia cyfra pesel: {pesel[-1:]}")
pesel_check = 10 - int(last_pesel_number_str[-1:])
print(f"pesel check number: {pesel_check}")

print(f"pesel: {type(pesel)}")
print(f"pesel_check: {type(pesel_check)}")
print('\n')

print(f"twój pesel: {pesel} => pesel check number {pesel_check}")
pesel_check = str(pesel_check)
# check if the last digit of pesel is equal to pesel_check_pattern_part_one
if pesel[-1:] == pesel_check:
    print(f"Twój pesel: {pesel} jest poprawny")
else:
    print(f"Twój pesel: {pesel} jest niepoprawny")

print('\n')
print(f"pesel: {type(pesel)}")
print(f"pesel_check: {type(pesel_check)}")
