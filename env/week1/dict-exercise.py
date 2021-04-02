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

word=input('Wpisz szukane słowo: ')
if word in word_list:
    print(f'{word} to: {word_list[word]}')
if word in word_list.values():
    print(f'{word_list[word]} ')
