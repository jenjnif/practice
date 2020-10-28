# add up the two unique values in array where there cannot be more the two occurances of an individual number

input_array = [4,5,7,5,4,8]

# solve with dictionary - works with multiple duplicates - O(n)

def add_unique_numbers_dict(input_array):
    dictionary = {}
    unique = 0
    for number in input_array:
        dictionary[number] = dictionary.get(number, 0) + 1
    for (key, value) in dictionary.items():
        if value == 1:
            unique += key
    return unique

print(add_unique_numbers_dict(input_array))


# solve with set - O(n)

def add_unique_numbers_set(input_array):
    have_seen = set()

    for number in input_array:
        if number in have_seen:
            have_seen.remove(number)
        else:
            have_seen.add(number)
    return sum(have_seen)

print(add_unique_numbers_set(input_array))


# solve by checking against ordered list - O(n logn)
def add_unique_numbers_ordered_array(input_array):
    input_array.sort()
    unique_nums_total = 0
    index = 0

    while index < len(input_array):
        if index == len(input_array)-1 or input_array[index] != input_array[index+1]:
            unique_nums_total += input_array[index]

        else:
            index += 1

        index += 1

    return unique_nums_total

print(add_unique_numbers_ordered_array(input_array))
