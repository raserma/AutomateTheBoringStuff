#!/usr/bin/env python3
# A loop into a loop. It rotates the input grid 90 degrees.

# Number of rows: len(grid)
# Number of cols: len(grid[0])

def print_picture_grid(my_list):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            print(my_list[y][x], end='')
        print()


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print_picture_grid(grid)
