#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a 2D square matrix 90 degrees clockwise in place.
    Args:
        matrix (list of list of int): The 2D square matrix to rotate.
    Returns:
        None
    """
    n = len(matrix)
    
    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to achieve the 90-degree rotation
    for i in range(n):
        matrix[i].reverse()

