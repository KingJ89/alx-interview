#!/usr/bin/python3
"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given total.
    Args:
        coins (list of ints): A list of coin values.
        total (int): The total value to be met.
    Returns:
        int: Minimum number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0
    
    if not coins:
        return -1
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    coin_count = 0
    
    for coin in coins:
        if total <= 0:
            break
        # Use as many of this coin as possible
        coin_count += total // coin
        total %= coin
        # If there's any total left, it means we cannot meet the target
    return coin_count if total == 0 else -1
