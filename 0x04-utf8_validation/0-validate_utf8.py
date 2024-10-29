#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """Checks if a list of integers represents valid UTF-8 encoded data."""
    skip = 0
    for byte in data:
        if skip > 0:
            if byte & 0b11000000 != 0b10000000:
                return False
            skip -= 1
        else:
            if byte < 0x80:
                continue  # 1-byte character
            elif byte & 0b11111000 == 0b11110000:
                skip = 3  # 4-byte character
            elif byte & 0b11110000 == 0b11100000:
                skip = 2  # 3-byte character
            elif byte & 0b11100000 == 0b11000000:
                skip = 1  # 2-byte character
            else:
                return False  # Invalid starting byte

    return skip == 0

