# this is a function to find the number at a given x,y co-ordinate
example_grid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def find_my_number(x, y, example_grid):

    number = example_grid[x+(4*y)]

    return number


def test_find_my_number_examples():
    assert find_my_number(2, 2, example_grid) == 11


def test_easiest_case():
    assert find_my_number(0, 0, example_grid) == 1


def test_second_number():
    assert find_my_number(1, 0, example_grid) == 2


def test_first_number_second_line():
    assert find_my_number(0, 1, example_grid) == 5


def test_first_number_third_line():
    assert find_my_number(0, 2, example_grid) == 9


"""
1   2  3  4
5   6  7  8
9  10 11 12
13 14 15 16

"""
