
# kuba siedem osiem kuba agata kozak kuba


# def word_counter(str):
#     counts = dict()
#     words = str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts


input_string = input("wpisz słowa, których występowanie będzie policzone ")
counts = dict()
words = input_string.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
print(type(counts))

for item in counts.items():
    print(f"{item[0]} = {item[1]}")
