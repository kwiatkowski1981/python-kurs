pesel = input("podaj pesel: ")
print(type(pesel))
print(pesel)
pesel_digits_sum = (int(pesel[0]) * 1) + (int(pesel[1]) * 3) + \
                    (int(pesel[2]) * 7) + (int(pesel[3]) * 9) + \
                    (int(pesel[4]) * 1) + (int(pesel[5]) * 3) + \
                    (int(pesel[6]) * 7) + (int(pesel[7]) * 9) + \
                    (int(pesel[8]) * 1) + (int(pesel[9]) * 3)

pesel_digits_sum_as_string = str(pesel_digits_sum)
last_sum_digit = pesel_digits_sum_as_string[-1:]
check_number = 10 - int(last_sum_digit[-1:])
check_number_as_str = str(check_number)
if pesel[-1:] == check_number_as_str:
    print(f"Twój pesel: {pesel} jest poprawny")
else:
    print(f"Twój pesel: {pesel} jest niepoprawny")

quit()
# 81042108198
