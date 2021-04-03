from collections import Counter


# name = input('podaj imie: ')
# greetings = "Dzien dobry"
#
# if name == 'kuba':
#     print(f"{greetings} panie {name}")
# elif name[-1:] == 'a':
#     print(f"{greetings} pani {name}")
# else:
#     print(f"{greetings} panie {name}")
#
#
# password = input('podaj hasło do zaszyfrowania: ')
# new_password = password.replace('a', '@')
# new_password = new_password.replace('s', '$')
# print(new_password)


sentence = "Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie."
print(sentence)
sentence_lower = sentence.lower()
print(sentence_lower.find('pies'))
# for id, sent in enumerate(sentence_lower):
#     print(id, sent, end=' ')
print(sentence_lower)


sentence_lower.count("pies")
words = sentence_lower.split()
print(words)
wordCount = Counter(words)
print(f" tyle ==> {wordCount}")
# print(f"ilosc najczesciej powtarzanych {wordCount}")

for word3, id in sorted(wordCount.items(), key=lambda item: item[1], reverse=True):
    print(word3, id, sep=" | ")

print('\n')

test_str = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'
print("orygilnalne zdanie : " + str(test_str))

result = any(chr.isdigit() for chr in test_str)     # sprawdzam na zawartosc cyfr w stringu
result2 = [int(i) for i in test_str.split() if i.isdigit()]     # robie liste z zawartymi w stringu cyframi

print("Czy moje zdanie zawiera cyfry? : " + str(result))
print("moje cyfry to : " + str(result2))
print(f"Suma moich cyfr to: {sum(result2)}")
