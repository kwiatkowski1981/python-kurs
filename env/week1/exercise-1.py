numbers = tuple(range(12, 1024, 6))  # stwórz tuplezawierajaca liczby podzielne przez 6 z zakresu od 12 do 1024
print(numbers)  # wyswietl liczby z tupli
print(len(numbers))  # ile jest tych liczb
print(numbers[0: 3])  # wyswietl pierwsze 3 liczby
print(min(numbers))  # wyswietl min (pierwsza, najmniejsza)
print(max(numbers))  # wyswietl max (ostatnia, najwieksza)
print(max(numbers[: -1]))  # wyswietl przedostatnia
print(numbers[3:: 6])  # wyswietl co 6 element liczac od 4
print(numbers[max(numbers): 0: -3])  # wyswietl co 3 od konca
print(numbers[max(numbers): -11: -1])  # wyswietl ostatnie 10
print(sum(numbers[max(numbers): -11: -1]) / len(numbers[max(numbers): -11: -1]))  # wyswietl srednią ostatnich 10
