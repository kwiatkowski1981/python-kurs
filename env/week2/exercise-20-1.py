div_by_3 = set(range(3, 1000, 3))
print(div_by_3)


def find_divisors(a):
    # divisors = set()
    # for divisor in range(2, a + 1):
    #     if a % divisor == 0:
    #         divisors.add(divisor)
    #
    # return divisors
    return {divisor for divisor in range(2, a + 1) if a % divisor == 0}


def calculate_common_divisor(a, b, offset=2):
    common_divisors = find_divisors(a) & find_divisors(b)
    common_divisors = [divisor for divisor in common_divisors if divisor >= offset]
    return sorted(common_divisors) if len(common_divisors) > 0 else None


test1 = calculate_common_divisor(3, 6)
print(test1)

test2 = calculate_common_divisor(a=3, b=6, offset=4)
print(test2)

test3 = calculate_common_divisor(8, 16)
print(test3)

test4 = calculate_common_divisor(132, 132, 4)
print(test4)


def calculate_brutto(netto: int, vat: float) -> float:
    return netto + netto * vat


print(calculate_brutto(100, 0.23))
print(calculate_brutto(120.30, 0.23))
