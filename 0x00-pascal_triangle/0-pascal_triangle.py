#!/usr/bin/python3

"""Pascal's Triangle Module"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    
    Args:
        n (int): Number of rows for Pascal's triangle.
    
    Returns:
        list: A list of lists where each inner list represents a row in Pascal's triangle.
        If n <= 0, an empty list is returned.
    """
    # Return an empty list for non-positive n
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows of Pascal's triangle
    for _ in range(1, n):
        # Use zip to calculate the next row based on the previous one
        prev_row = triangle[-1]
        new_row = [a + b for a, b in zip([0] + prev_row, prev_row + [0])]
        triangle.append(new_row)
    
    return triangle

