# from 2d_array_basic import find_my_number

# this is a function to find the number at a given x,y co-ordinate
example_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def find_my_number(x, y, example_grid):

    number = example_grid[x+(4*y)]

    return number


def list_my_cross(x, y, example_grid):

    original_top_numbers = []
    original_top_numbers.append(find_my_number(x, y, example_grid))

    if (y-1) >= 0:
        top_number = find_my_number(x, y-1, example_grid)
        original_top_numbers.append(top_number)

    if (x-1) >= 0:
        left_number = find_my_number(x-1, y, example_grid)
        original_top_numbers.append(left_number)

    if ((y+1)*4) <= (len(example_grid)-4):
        bottom_number = find_my_number(x, y+1, example_grid)
        original_top_numbers.append(bottom_number)

    if ((x+1)*4) <= (len(example_grid)-4):
        right_number = find_my_number(x+1, y, example_grid)
        original_top_numbers.append(right_number)

    return original_top_numbers


def sum_of_cross(x, y, example_grid):

    return sum(list_my_cross(x, y, example_grid))


def highest_sum_cross(example_grid):

    highest_sum_cross = 0
    x = 0
    y = 0

    for coordinate in example_grid:

        print('x is ' + str(x))

        print('y is ' + str(y))
        current = sum_of_cross(x, y, example_grid)
        if current > highest_sum_cross:
            highest_sum_cross = current
            highest_sum_coordinate = [x, y, highest_sum_cross]
        if x < 3:
            x += 1
        else:
            x = 0
            y += 1
    return highest_sum_coordinate


def test_find_starting_number():
    assert find_my_number(2, 2, example_grid) == 11


def test_include_top_neighbour():
    assert list_my_cross(2, 2, example_grid)[1] == 7


def test_include_left_neighbour():
    assert list_my_cross(2, 2, example_grid)[2] == 10


def test_include_bottom_neighbour():
    assert list_my_cross(2, 2, example_grid)[3] == 15


def test_include_right_neighbour():
    assert list_my_cross(2, 2, example_grid)[4] == 12


def test_include_all_neighbours():
    assert list_my_cross(2, 2, example_grid) == [11, 7, 10, 15, 12]


def test_include_all_neighbours_length():
    assert len(list_my_cross(2, 2, example_grid)) == 5


def test_start_no_top_neighbour():
    assert find_my_number(1, 0, example_grid) == 2


def test_no_top_neighbour():
    assert len(list_my_cross(1, 0, example_grid)) == 4


def test_start_no_left_neighbour():
    assert find_my_number(0, 1, example_grid) == 5


def test_no_left_neighbour():
    assert len(list_my_cross(0, 1, example_grid)) == 4


def test_start_no_bottom_neighbour():
    assert find_my_number(1, 3, example_grid) == 14


def test_no_bottom_neighbour():
    assert len(list_my_cross(1, 3, example_grid)) == 4


def test_start_no_right_neighbour():
    assert find_my_number(3, 1, example_grid) == 8


def test_no_right_neighbour():
    assert len(list_my_cross(3, 1, example_grid)) == 4


def test_sum_cross():
    assert sum_of_cross(2, 2, example_grid) == (11+7+10+15+12)


def test_highest_sum():
    assert highest_sum_cross(example_grid)[2] == 56


def test_highest():
    assert highest_sum_cross(example_grid) == [2, 3, 56]


"""
1   2  3  4
5   6  7  8
9  10 11 12
13 14 15 16

"""
