def find_cell(x, y, table):

    number = example_grid[x][y]
    return number


example_grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def test_multidimensional_array_access():
    assert find_cell(2, 2, example_grid) == 11
