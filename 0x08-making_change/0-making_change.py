#!/usr/bin/python3
"""
coin change
"""


def makeChange(coins, total):
    """
    count the number of coins
    """
    coins.sort(reverse=True)
    i = 0
    count = 0
    sum = 0
    init_tot = total
    if total == 0 or total < 0:
        return 0
    while i < len(coins):
        if total - coins[i] >= 0:
            count += 1
            total -= coins[i]
            sum += coins[i]
        else:
            i += 1

    if sum != init_tot:
        return -1
    return count
