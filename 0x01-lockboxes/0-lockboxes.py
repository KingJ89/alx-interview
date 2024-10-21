#!/usr/bin/python3
"""
This module defines a method to determine if all boxes can be unlocked.
Each box is numbered sequentially from 0 to n - 1 and may contain keys to other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists where each inner list contains the keys inside a particular box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Return False if input is not a list or is empty
    if not isinstance(boxes, list) or not boxes:
        return False

    # Track the boxes that can be unlocked, starting with the first one (0)
    unlocked = [0]

    # Explore all the boxes that have been unlocked
    for box in unlocked:
        for key in boxes[box]:
            # Add the key to unlocked if it's not already unlocked and within valid range
            if key < len(boxes) and key not in unlocked:
                unlocked.append(key)
    
    # Return True if all boxes are unlocked, otherwise False
    return len(unlocked) == len(boxes)
