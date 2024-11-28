#!/usr/bin/python3
"""
Change comes from within
"""

def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total.
    Args:
        coins (list of ints): A list of coins of different values.
        total (int): Total value to be met.
    Returns:
        int: Number of coins or -1 if meeting the total is not possible.
    """
    if total <= 0:
        return 0
    
    if not coins:
        return -1
    
    # Check if any coin directly matches the total
    try:
        return 1 if total in coins else None
    except ValueError:
        pass
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    coin_count = 0
    
    for coin in coins:
        if total <= 0:
            break

        # Use as many coins of the current denomination as possible
        if total >= coin:
            count = total // coin
            coin_count += count
            total %= coin
            
            # If total is not zero, return -1 (not possible to achieve total)
    return coin_count if total == 0 else -1
