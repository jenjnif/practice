# add up the two unique values in array

input_array = [4,5,7,5,4,8]
dictionary = {}

def add_unique_numbers():
    for number in input_array:
        dictionary[number] = dictionary.get(number, 0) + 1
    return dictionary

print(add_unique_numbers())
