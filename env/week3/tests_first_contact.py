def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers():
    # given
    a = 2
    b = 3
    # when
    value = add_numbers(a, b)
    # then
    assert value == 5
