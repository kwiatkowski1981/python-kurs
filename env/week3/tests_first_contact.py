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


def count_letters(text, start='(', end=')'):
    should_count = False
    counter = 0
    temp_counter = 0
    for char in text:
        if char == end:
            should_count = False
            counter += temp_counter
            temp_counter = 0

        if should_count:
            temp_counter += 1

        if char == start:
            should_count = True

    return counter


def test_barteks_idea():
    assert count_letters('Samuraj (Programowania') == 0


def test_count_letters_once():
    assert count_letters('Samuraj (Programowania)') == 13


def test_count_letters_none():
    assert count_letters('Samuraj') == 0


def test_count_letters_override():
    assert count_letters('Python', '>', '<') == 0


def test_multiple_brackets():
    assert count_letters('(Python) jest (super) silnym (językiem) programowania(!)(!)') == 21
    assert count_letters('<Python> jest <super> silnym <językiem> programowania<!>', '<', '>') == 20
