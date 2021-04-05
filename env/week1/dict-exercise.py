
word_list = {
    'czerwony': 'rot',
    'zielony': 'grün',
    'niebieski': 'blau',
    'żółty': 'gelb',
    'szary': 'grau',
    'biały': 'weiß',
    'czarny': 'schwarz',
    'pomarańczowy': 'orange',
    'beżowy': 'beige',
    'brązowy': 'braun'
}


word = input('Wpisz szukane słowo: ')
if word in word_list:
    print(f'{word} to: {word_list[word]}')       # todo else


for word in word_list.items():
    print(f"{word[0]}: {word[1]}")
