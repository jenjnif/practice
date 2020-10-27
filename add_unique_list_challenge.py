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
    unique_array = []
    index = 0

    while index < len(input_array):
        if index == len(input_array)-1:
            unique_array.append(input_array[index])
            break

        if input_array[index] == input_array[index+1]:
            index += 2

        else:
            unique_array.append(input_array[index])
            index += 1


    total = sum(unique_array)

    return total

print(add_unique_numbers_ordered_array(input_array))
