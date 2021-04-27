def calculate_electricity_cost(hours_spent: float, consumption: float, price: float = 0.617) -> float:
    return hours_spent * consumption * price


print(calculate_electricity_cost(8, 0.5, 0.617))
print(calculate_electricity_cost(8, 2))


def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    odds = [number for number in numbers if number % 2 != 0]
    even = [number for number in numbers if number % 2 == 0]

    total = 0 if not count_odd else len(odds)
    total += 0 if not count_even else len(even)

    return total


print(count_numbers([1, 2, 3, 4, 5, 6]))
print(count_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], count_odd=False))
print(count_numbers([1, 2, 3, 4, 5, 6], count_even=False))
