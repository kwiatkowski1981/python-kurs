numbers = tuple(range(12, 1025, 6))  # stwórz tuplezawierajaca liczby podzielne przez 6 z zakresu od 12 do 1024
print(numbers)  # wyswietl liczby z tupli
print(len(numbers))  # ile jest tych liczb
print(numbers[0: 3])  # wyswietl pierwsze 3 liczby
print(min(numbers))  # wyswietl min (pierwsza, najmniejsza)
print(max(numbers))  # wyswietl max (ostatnia, najwieksza)
print(max(numbers[: -1]))  # wyswietl przedostatnia
print(numbers[-2])  # wyswietl przedostatnia ( krotszy zapis !!! )
print(numbers[3:: 6])  # wyswietl co 6 element liczac od 4
print(numbers[max(numbers): 0: -3])  # wyswietl co 3 od konca
print(numbers[::-3])  # wyswietl co 3 od konca ( krotszy zapis !!! )

print(numbers[max(numbers): -11: -1])  # wyswietl ostatnie 10 / reverse
print(tuple(reversed(numbers[-10:])))  # wyswietl ostatnie 10 / reverse /// how todo / done

print(numbers[-10:])  # wyswietl ostatnie 10 elementow
print(sum(numbers[max(numbers): -11: -1]) / len(numbers[max(numbers): -11: -1]))  # wyswietl srednią ostatnich 10
print(sum(numbers[-10:]) / len(numbers[-10:]))  # wyswietl srednią ostatnich 10 ( krotszy zapis !!! )
