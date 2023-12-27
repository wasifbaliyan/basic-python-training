# Exception handling
numbers = [1, 2]

try:
    print(numbers[3])
except IndexError as ex:
    print("Oops, this value doesn't exist in the array", ex)


try:
    file = open("data.csv")
    age = int(input("Enter you age: "))

    magic_number = 10//age
    print(magic_number)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Age cannot be zero.")
except FileNotFoundError:
    print("File doesn't exist.")
except TypeError as ex:
    print(ex)
else:
    print("After successful run")
finally:
    file.close()

print("Contnd...")
