#!/usr/bin/python3
"""Island perimeter computing module."""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.

    Args:
        grid (list of list of int): A 2D grid representing the map
                                    (1 for land, 0 for water).

    Returns:
        int: The perimeter of the island.
    """
    if not isinstance(grid, list) or not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Only process land cells
                # Check all four edges
                if i == 0 or grid[i - 1][j] == 0:  # Top edge
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right edge
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom edge
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left edge
                    perimeter += 1

    return perimeter
