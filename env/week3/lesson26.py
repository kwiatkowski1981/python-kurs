from collections.abc import Callable
from functools import reduce

# Callable[[argument_type], return_type]


def do_something(data: list, f: Callable[[list], int]):
    return f(data)


print(do_something([1, 2, 3], sum))
print(do_something([4, 5, 6], len))


def total_salary(base, calculate_extra):
    return base + calculate_extra(base)


def calculate_ten_percent(amount):
    return 0.1 * amount


def calculate_zero(amount):
    return 0


# Bartek
print(total_salary(1000, calculate_ten_percent))

# bez premii
print(total_salary(1000, calculate_zero))

# lambda

power = lambda x: x**2
print(power(10))

sum_numbers = lambda a, b: a + b
print(sum_numbers(23, 34))


numbers = [1, 5, 10, 9, 7, 2]
doubles_lc = [n + n for n in numbers]
print(doubles_lc)
doubles_map = map(lambda n: n + n, numbers)
print(list(doubles_map))        # jeśli nie "wrzucę" listy to zwróci mi jak poniżej adres obiektu
print(map(lambda n: n + n, numbers))
filtered_lc = [n for n in numbers if n % 2 == 0]
print(filtered_lc)
filtered_filter = filter(lambda n: n % 2 == 0, numbers)
print(list(filtered_filter))        # jeśli nie "wrzucę" listy to zwróci mi jak poniżej adres obiektu
print(filter(lambda n: n % 2 == 0, numbers))

numbers_2 = [
    (1, 2),
    (3, 4),
    (5, 6)
]
total_lc = sum([a * b for a, b in numbers_2])
print(f'total: {total_lc}')
total_reduce = reduce(lambda sum, a: sum + a[0] * a[1], numbers_2, 0)
print(total_reduce)

names = ['Leon', 'Barbara', 'Czesław', 'Fryderyk']
by_alphabet = sorted(names)
by_last_letter = sorted(names, key=lambda x: x[-1])
by_length = sorted(names, key=len)
print(f'by_alphabet: {by_alphabet}')
print(f'by_last_letter: {by_last_letter}')
print(f'by_length: {by_length}')

