# add up the two unique values in array

input_array = [4,5,7,5,4,8]

# solve with dictionary
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


# solve with set
have_seen = set()

def add_unique_numbers_set(input_array):
    for number in input_array:
        if number in have_seen:
            have_seen.remove(number)
        else:
            have_seen.add(number)
    return sum(have_seen)

print(add_unique_numbers_set(input_array))


# solve by checking against ordered list
def add_unique_numbers_ordered_array(input_array):
    input_array.sort()
    return input_array

print(add_unique_numbers_ordered_array(input_array))
