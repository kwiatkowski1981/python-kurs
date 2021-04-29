from collections.abc import Callable

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
