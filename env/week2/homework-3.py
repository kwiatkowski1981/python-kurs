
def get_factorial(number):
    result = 1
    while number >= 1:
        result = result * number
        print(f" result: {result} = result: {result} * number - 1: {number - 1}")
        number -= 1
        print(f"number {number}")
    return result


factorial = get_factorial(int(input("podaj cyfre: ")))
print(f"wynik = {factorial}")
