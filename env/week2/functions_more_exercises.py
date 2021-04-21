from typing import Union


def get_salary(hours, hourly_rate=25.0):
    return hours * hourly_rate


def calculate_tax(salary, tax_rate=0.19):
    return salary - salary * tax_rate


hours = float(input('ilość przepracowanych godzin: '))
rate = float(input('Twoja stawka godzinowa: '))

salary_with_tax = get_salary(hours, rate)
salary_netto = calculate_tax(salary_with_tax)

print('Twoje wynagrodzenie wynosi:')
print(f'brutto: {salary_with_tax}')
print(f'netto: {salary_netto}')


def add_numbers(a: int, b: int) -> int:
    return a + b


def calculate_length(a: str) -> int:
    return len(a)


def is_adult(age: int) -> bool:
    return age >= 18


def print_data(something: Union[int, str]):
    print('Czas na wyświetlenie! ')
    print(something)


print_data('Kuba')
print_data(123)
print_data(True)


def car_details():
    return {
        'brand': 'Fiat',
        'model': '126p',
        'nickname': 'Maluch'
    }


def get_car_size():
    width = 1377
    height = 1335
    length = 3054
    return width, height, length


car_width, car_height, car_length = get_car_size()

details = car_details()
print(details)
print(car_length)
print(car_width)
print(car_height)
maluch = get_car_size()
print(maluch)
print(maluch[0])
print(maluch[1])
print(maluch[2])
