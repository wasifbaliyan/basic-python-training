import random
import string
import math


num = 0

choice = random.choice([1, 3, 4])
choices = random.choices(string.ascii_letters + string.digits, k=6)
range = random.randrange(1, 30)
intr = random.randint(1, 20)
print("choice", "".join(choices))

# while num != 1:
#     print(num)
#     num = math.floor(random.random() * 10) + 1
