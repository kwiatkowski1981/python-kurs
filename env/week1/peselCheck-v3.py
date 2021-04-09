# pesel = input("podaj pesel: ")

pesel = str("81042108198")


pesel = input("podaj pesel: ")
pesel_pattern_digits = ['1', '3', '7', '9', '1', '3', '7', '9', '1', '3']
pesel_digits_to_multiply = list(zip(list(pesel), pesel_pattern_digits))
multiplied_pesel_digits = []
for pesel_number, pattern_digit in pesel_digits_to_multiply:
    multiplied_pesel_digits.append(int(pesel_number) * int(pattern_digit))
pesel_digits_sum = sum(multiplied_pesel_digits)
pesel_digits_sum_as_string = str(pesel_digits_sum)
last_sum_digit = pesel_digits_sum_as_string[-1:]
check_number = 10 - int(last_sum_digit[-1:])
check_number_as_str = str(check_number)
if pesel[-1:] == check_number_as_str:
    print(f"Twój pesel: {pesel} jest poprawny")
else:
    print(f"Twój pesel: {pesel} jest niepoprawny")


# 81042108198       pesel
# 1379137913        mnożnik
# 8303623072127     wynik
