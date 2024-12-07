#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0 (water) or 1 (land)
    Return:
        the perimeter of the island
    Author: Kedir Jabir (IbnuJabir)
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check if there's land above, subtract 2 if so
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                # Check if there's land to the left, subtract 2 if so
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
