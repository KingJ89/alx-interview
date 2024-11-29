#!/usr/bin/python3
"""
This script determines the minimum number of coins needed to make a total value.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to reach a specified total value.
    Args:
        coins (list of ints): A list containing different coin values.
        total (int): The total value to be achieved.
    Return:
        The minimum number of coins required to meet the total, or -1 if it is not possible to meet the total.
    """
    if total <= 0:
        return 0  # No coins needed for a zero or negative total
    if coins == [] or coins is None:
        return -1  # No coins available or list is empty
    try:
        n = coins.index(total)  # Check if the total is directly in the list of coins
        return 1  # If the total is found in the coin list, only one coin is needed
    except ValueError:
        pass  # If the total is not found, continue to try to make the change

    coins.sort(reverse=True)  # Sort coins in descending order to try larger coins first
    coin_count = 0  # Counter to keep track of the number of coins used
    for i in coins:
        if total % i == 0:  # If the total is divisible by the coin value
            coin_count += int(total / i)  # Add the number of coins needed for this value
            return coin_count  # Return the result as the total can be exactly divided
        if total - i >= 0:  # If the current coin can be subtracted from the total
            if int(total / i) > 1:  # If more than one coin of this type is needed
                coin_count += int(total / i)  # Add the required number of coins
                total = total % i  # Reduce the total by the amount covered by these coins
            else:
                coin_count += 1  # Use one coin of this value
                total -= i  # Subtract the coin value from the total
                if total == 0:  # If the total is reduced to 0, stop
                    break
    if total > 0:  # If the total couldn't be made exactly, return -1
        return -1
    return coin_count  # Return the total number of coins used

