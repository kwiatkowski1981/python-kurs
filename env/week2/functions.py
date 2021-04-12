def get_doubles(numbers: range):
    for i in numbers:
        print(f"iteruje liczbe dla: {i}")
        yield i + i


results = get_doubles(range(111, 2222))

for n in get_doubles(range(1, 11)):
    print(f"wynik wynosi: {n}")

print("*" * 150)
print("*" * 150)
print("*" * 150)
print("*" * 150)
print("*" * 150)


print(next(results))
print(next(results))
print(next(results))
print(next(results))
print(next(results))
print(next(results))

