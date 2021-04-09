
people =[
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

# print(people)
# print(len(people))
#
# for item in people:
#     print(len(item), end=' ')
# print('.')


for item in people:
    if len(item) % 2 == 0:
        print(len(item))



    #     print(f"ilosc parzystych = {item.count(item)}")
    # else:
    #     print(len(item) / item.count(item))
        # print(f"nieparzyste {(len(item) / item.count(item))}", end=' ')
# print()

# items = [len(item) if len(item) % 2 == 0 else (sum(item) / len(item)) for item in people if len(item) > 2 < 6]
