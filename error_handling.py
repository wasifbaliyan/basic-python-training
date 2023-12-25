

def check_eligibility(age):
    if age <= 0:
        # raising exceptions can have a negative impact on performance, only do when necessary, try to ignore them by adding a check if possible
        raise ZeroDivisionError("Age cannot be zero or less")
    score = 100 / age
    print(score)


try:
    check_eligibility(0)
except ZeroDivisionError as error:
    print(error)
else:
    print("If try block runs this code will also run")
finally:
    print("Will always run")
