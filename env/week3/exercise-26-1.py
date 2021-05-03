def calculate_square_root(numbers):
    power = []
    for number in numbers:
        power.append(number ** 2)
        # print(power)
    return power


result = calculate_square_root([16, 36, 25, 49])
print(result)
print(list(filter(lambda x: x % 2 == 0, result)))


people = ['zofia nowak', 'kryStyna kowalska', 'michał lewandowski', 'michalina antończak']
# sorted_by_lastname = sorted(people, key=lambda x: x.split(' ')[-1])


def upper_first_letters(names):
    correct_writen_names = []
    for name in people:
        correct_writen_names.append(name.title())
        sorted_by_lastname = sorted(correct_writen_names, key=lambda x: x.split(' ')[-1])
    return sorted_by_lastname


print(list(upper_first_letters(people)))


