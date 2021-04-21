
peoples =[
    ('janusz', 'typowy', 'polska', 'pies', 'kot', 'strażak', 'sportowiec'),
    ('dorota', 'kuźniak', 'polska', 'papuga', 'mysz', 'nauczycielka'),
    ('michal', 'słowik', 'niemcy', 'wąż', 'programista', 'sportowiec'),
    ('dorota', 'czuba', 'polska', 'tenisistka', '25'),
    ('michal', 'duduś', 'usa', 'dziennikarz', '33'),
    ('kuba', 'wojewódzki', 'dziennikarz', 'kot'),
    ('brunhilda', 'stefańczuk', '23'),
    ('Janek', 'Wiśniewski', 'gdynia'),
    ('Grzegorz', 'Turnau', 'Kraków'),
    ('Syrenka', 'Warszawska', 'Warszawa'),
    ('Stefan', 'Rybka'),
    ('miecz', 'zbroja', 'tarcza'),
    ("tarcza", "zbroja", "miecz", "hełm"),
    ('pies', '5', 'kot', 'jeż', '77', 'pająk', '8.4'),
    ('Jan', 'Nowak'),
    ('Monika', 'Czekan', '1974'),
    ('Anna', 'Solas'),
    ('niunia',)
]


numbers = [
    (1,),
    (1, 2, 3, 4),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6, 7, 8, 9,),
    (1, 2, 3, 4, 5, 6, 7, 8, 9,),
    (1, 2, 3, 4, 5, 6, 7, 8, 9,),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5),
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5,),
    (1, 2, 3, 4, 5,),
    (1, 2, 3, 4),
    (1, 2, 3, 4),
    (1, 2, 3, 4),
]

# even1 = [people for people in peoples if len(people) % 2 == 0]
# print(even1)
# print(len(even1))
# odd2 = [people for people in peoples if len(people) % 2 != 0]
# print(odd2)
# print(len(odd2))

result = [sum(item) if len(item) % 2 == 0 else sum(item) / len(item) for item in numbers if 1 < len(item) < 6]
items = [sum(item) if len(item) % 2 == 0 else (sum(item) / len(item)) for item in numbers if len(item) > 2 if len(item) < 6]
print(items)
print(result)
