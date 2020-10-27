# add up the two unique values in array

input_array = [4,5,7,5,4,8]
dictionary = {}

def add_unique_numbers_dict(input_array):
    unique = 0
    for number in input_array:
        dictionary[number] = dictionary.get(number, 0) + 1
    for (key, value) in dictionary.items():
        if value == 1:
            unique += key
    return unique

print(add_unique_numbers_dict(input_array))


have_seen = set()
have_not_seen = set()

def add_unique_numbers_set(input_array):
    for number in input_array:
        have_seen.add(number)
    return have_seen

print(add_unique_numbers_set(input_array))
