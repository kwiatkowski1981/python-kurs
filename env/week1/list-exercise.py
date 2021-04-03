numbers = list(range(1, 100 +1))
print(numbers)
print('\n')
number_counter_div_4 = 0
number_counter_div_5 = 0

for number in numbers:
    if number % 4 == 0:
        print(number, end=', ')
        number_counter_div_4 += 1
print('\n', end="")
print(f"ilosc liczb podzielnych przez 4 to: {number_counter_div_4}")
print('\n')
for number in numbers:
    if number % 5 == 0:
        print(number, end=', ')
        number_counter_div_5 += 1
print('\n', end="")
print(f"ilosc liczb podzielnych przez 5 to: {number_counter_div_5}")
print('\n')
names = ['tomek', 'ola', 'agata', 'kuba', 'zosia', 'marysia', 'karol', 'oliver', 'matylda', 'bronislaw']
print(names)

if not names:
    print(f"w liście '{names}' nie ma jeszcze żadnych inmion")
else:
    print(min(names))   # alfabetycznie pierwsze
    print(max(names))   # alfabetycznie ostatnie
    print(min(names, key=len))      # najkrotsze
    print(max(names, key=len))      # najdluzsze
print('\n')

num = int(input('podaj liczbe: '))
print(num)

if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

print('\n')

books = ['frunky furbo', 'magiczny kod', 'kryształy czasu']
for number, book in enumerate(reversed(books), start=1):        # mozna uzyc sorted
    print(number, book)

