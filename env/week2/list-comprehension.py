# example 1
doubles = []
for n in range(1, 11):
    doubles.append(n+n)
print(doubles)

doubles2 = [n+n for n in range(1, 11)]
print(doubles2)

print([n+n for n in range(1, 11)])


# example 2
new_list = []
for n in range(1, 11):
    if n % 2 == 0:
        new_list.append(str(n) + ' = even')
    else:
        new_list.append(str(n) + ' = odd')

print(new_list)

new_list2 = [str(n) + ' = even' if n % 2 == 0 else str(n) + ' = odd' for n in range(1, 11)]
print(new_list2)

# example 3
names = ['Janek', 'Inga', 'Krzysiek', 'Basia']
ladies = []
for name in names:
    if name[-1:] == 'a':
        ladies.append(name)
print(ladies)
print([name for name in names if name[-1:] == 'a'])

persons = [
    ('Janek', 'Wiśniewski', 'gdynia'),
    ('Grzegorz', 'Turnau', 'Kraków'),
    ('Syrenka', 'Warszawska', 'Warszawa'),
    ('Stefan', 'Rybka', 'Gietrzwałd')
]

persons_g = [person for person in persons if person[-1][0].lower() == 'g']
print(persons_g)
person_upp = [(person[0], person[1], person[2].upper()) for person in persons_g]
print(person_upp)
person_2_in_1 = [(person[0], person[1], person[2].upper()) for person in persons if person[-1][0].lower() == 'g']
print(person_2_in_1)
