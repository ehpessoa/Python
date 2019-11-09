#! python3
# character_picture_grid.py - Converts a list to a rotated printout

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['0', '0', '0', '0', '0', '.'],
    ['.', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '.'],
    ['0', '0', '0', '0', '.', '.'],
    ['.', '0', '0', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]


def character_picture_grid(input_grid):
    """
    Prints grid list as strings
    :param input_grid: list of lists of string
    :return: None
    """
    for i in range(len(input_grid[0])):
        line = ''
        for row in input_grid:
            line += row[i]
        print(line)


character_picture_grid(grid)
