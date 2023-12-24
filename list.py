numbers = list(range(50))


for number in numbers:
    if (number % 2 == 0):
        print(number)


even_numbers = list(filter(lambda item: item % 2 == 0, numbers))

print(even_numbers)
