#!/usr/bin/python3
"""Prime Game alx intranet case"""


def isWinner(x, nums):
    """the Prime game function
    x is the number of rounds
    nums is the array of n"""
    if not nums or x < 1:
        return None
    bools = True
    count = 1
    flag = True
    primes = seive(nums)
    for i in primes:
        if count < x:
            for j in nums:
                if j % i == 0:
                    flag = False
                    nums.remove(j)
            if not flag:
                bools = not bools
                count += 1
            flag = True
    if count == 1 and bools:
        return "Ben"
    if bools:
        return "Maria"
    else:
        return "Ben"


def seive(array):
    """gets a list of prime numbers"""
    n = max(array)
    p = 2
    truth_table = [True for i in range(n + 1)]
    while p**2 <= n:
        if truth_table[p]:
            for i in range(p**2, n + 1, p):
                truth_table[i] = False
        p += 1
    prime_list = [i for i in range(2, n + 1) if truth_table[p]]
    return prime_list
