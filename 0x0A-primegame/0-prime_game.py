#!/usr/bin/python3
"""Prime game module.
"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    # Generate prime numbers up to the maximum value in nums
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for multiple in range(i * i, max_num + 1, i):
                primes[multiple] = False

    # Precompute the cumulative count of primes up to each number
    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Determine the winner for each round
    for n in nums[:x]:
        primes_count = prime_counts[n]
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
