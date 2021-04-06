word_to_encrypt = input("podaj słowo do zaszyfrowania: ")
encrypt_key = 3

# char_list = list(word_to_encrypt)
# print(char_list)
#
# for char in char_list:
#     encrypted_char = chr(ord(char) + encrypt_key)
#     print(encrypted_char, end='')
# print()

zaszyfrowany = ""
for i in range(len(word_to_encrypt)):
    if ord(word_to_encrypt[i]) > 122 - encrypt_key:
        zaszyfrowany += chr(ord(word_to_encrypt[i]) + encrypt_key - 26)
    else:
        zaszyfrowany += chr(ord(word_to_encrypt[i]) + encrypt_key)
print("Zaszyfrowany tekst ma wygląd:",zaszyfrowany)
