#!/usr/bin/python3
"""
island perimeter two
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a given grid.

    Args:
        grid: A 2D list representing the grid, where 1 indicates land and 0 indicates water.

    Returns:
        The perimeter of the island.
    """

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4  # Assume each land cell has a perimeter of 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 for shared sides with adjacent land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
