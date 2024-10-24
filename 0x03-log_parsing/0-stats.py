#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys

def print_metrics(total_size: int, status_codes: dict):
    """Prints the total file size and the count of each status code."""
    print(f'File size: {total_size}')
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f'{code}: {count}')

# Initialize the cache for status codes and total size
status_cache = {code: 0 for code in ['200', '301', '400', '401', '403', '404', '405', '500']}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        try:
            # Split the input line and extract status code and file size
            parts = line.split()
            if len(parts) > 1:
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Update status code counts and total file size
                if status_code in status_cache:
                    status_cache[status_code] += 1
                total_size += file_size
                line_counter += 1

            # Print metrics every 10 lines
            if line_counter == 10:
                print_metrics(total_size, status_cache)
                line_counter = 0

        except (IndexError, ValueError):
            # Ignore lines with invalid format
            continue

except KeyboardInterrupt:
    pass

finally:
    # Always print the metrics after finishing or on exit
    print_metrics(total_size, status_cache)

