class MyCustomError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message


def factorial(number):
    if number < 0:
        raise MyCustomError("Number can not be zero.")

    factor = 1
    for num in range(1, number+1):
        factor *= num

    return factor


try:
    result = factorial(-10)
    print(result)
except MyCustomError as ex:
    print(ex)
