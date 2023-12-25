from sys import getsizeof

values1 = {item: item**2 for item in range(21) if item % 2 != 0}


# Generator object -> use it when creating a very large list and you don't want to use alot of memory
# values = (item for item in range(20))
# for key in values:
#     print(key)
# print(getsizeof(values))


# problem find the most repeated character in a sentence

def find_repeated_char(str):
    if len(str) == 0:
        print(False)
        return
    freq = {}
    for letter in str:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    freq_list = list(freq.items())
    max_repeated = freq_list[0]

    for item in freq_list:
        if item[1] > max_repeated[1]:
            max_repeated = item

    print(max_repeated[0])


find_repeated_char("")
