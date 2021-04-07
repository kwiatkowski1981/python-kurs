pesel = input("podaj pesel: ")
print(type(pesel))
print(pesel)


def convert_pesel_to_list(pesel):
    pesel_as_list = list(pesel)
    print(pesel_as_list)
    return pesel_as_list


def pesel_pattern_sum_digits(pesel_as_list):
    pesel_digits_sum = (int(pesel_as_list[0]) * 1) + (int(pesel_as_list[1]) * 3) + \
                        (int(pesel_as_list[2]) * 7) + (int(pesel_as_list[3]) * 9) + \
                        (int(pesel_as_list[4]) * 1) + (int(pesel_as_list[5]) * 3) + \
                        (int(pesel_as_list[6]) * 7) + (int(pesel_as_list[7]) * 9) + \
                        (int(pesel_as_list[8]) * 1) + (int(pesel_as_list[9]) * 3)
    print(pesel_digits_sum)
    return pesel_digits_sum


def pesel_pattern_sum_digits_to_str(pesel_digits_sum):
    pesel_digits_sum_as_string = str(pesel_digits_sum)
    print(pesel_digits_sum_as_string)
    return pesel_digits_sum_as_string


def pesel_pattern_sum_last_digit(pesel_digits_sum_as_string):
    last_sum_digit = pesel_digits_sum_as_string[-1:]
    print(last_sum_digit)
    return last_sum_digit


def pesel_check_number(last_sum_digit):
    check_number = 10 - int(last_sum_digit[-1:])
    print(check_number)
    return check_number


def pesel_check_number_to_str(check_number):
    check_number_as_str = str(check_number)
    print(check_number_as_str)
    return check_number_as_str


def check_if_last_digit_of_pesel_is_equal_to_check_number_as_str( check_number_as_str):
    if pesel[-1:] == check_number_as_str:
        print(f"Twój pesel: {pesel} jest poprawny")
    else:
        print(f"Twój pesel: {pesel} jest niepoprawny")


# 81042108198
