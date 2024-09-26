#!/usr/bin/python3

def island_perimeter(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                total += scanner(grid, i, j)
    return total


def scanner(matrix, i, j):
    sum = 0
    if (j - 1 >= 0 and matrix[i][j - 1] == 0):
        sum += 1
    if (i - 1 >= 0 and matrix[i - 1][j] == 0):
        sum += 1
    if (j + 1 <= len(matrix[i]) - 1 and matrix[i][j + 1] == 0):
        sum += 1
    if (i + 1 <= len(matrix) - 1 and matrix[i + 1][j] == 0):
        sum += 1
    return sum
