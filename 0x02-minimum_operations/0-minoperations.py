#!/usr/bin/python3

"""
Module that calculates the fewest number of operatons
needed to result in exactly n 'H' characters in the file.
"""
def minOperations(n):
    """
    Determines the minimum number of operations needed to achieve exactly
    n 'H' characters in a file using only 'Copy All' and 'Paste' operations.
    
    Args:
    n (int): The target number of 'H' characters.
        
        Returns:
    int: The minimum number of opertions required. If n is les than or equal to 1, returns 0.
        """
        operations = 0
    min_operations = 2
    while n > 1:
        while n % min_operations == 0:
            operations += min_operations
            n /= min_operations
        min_operations += 1
    return operations
