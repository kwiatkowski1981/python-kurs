def log(*args, **kwargs):
    print(args)
    print(kwargs)
    for arg in args:
        print(type(arg), arg)
    for kwarg in kwargs:
        print(type(kwarg), kwarg)


log(1, 2, 3, hello='Bartek')
log('1', 2, 3, hello='Kacper')


def get_brutto(netto, vat):
    return netto + netto * vat


values = [
    (100, 0.23),
    (50, 0.5)
]

for value in values:
    print(get_brutto(*value))


def calculate_power(number):
    if number == 0:
        return 1
    return number * calculate_power(number - 1)


def test_power_zero():
    assert calculate_power(0) == 1


def test_power():
    assert calculate_power(1) == 1
    assert calculate_power(5) == 5 * 4 * 3 * 2 * 1

