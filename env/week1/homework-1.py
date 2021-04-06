
input_word = input("podaj słowo, w którym mają być policzone litery: ")
counts = dict()

for char in input_word:
    # print(char)
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(f"1) ==>  {counts}")
print(type(counts))

for key, value in counts.items():
    print(key, ' | ', value)
print('\n')

for item in counts.items():
    print(f"2) ==> : {item[0]} = {item[1]}")
print('\n')

for input_word, id in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    print(f'3) ==> : {input_word, id}', sep=" | ")
print(type(input_word))
