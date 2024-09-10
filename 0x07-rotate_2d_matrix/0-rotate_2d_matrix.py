#!/usr/bin/python3
"""matrix rotation"""

def rotate_2d_matrix(matrix):
    """test rotation
    """
    N = len(matrix)

    for i in range(N):
        for j in range(i, N):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(N):
        matrix[i] = matrix[i][::-1]