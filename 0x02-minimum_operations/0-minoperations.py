#!/usr/bin/python3
"""minimum operations"""


def minOperations(n):
    """in operations"""
    if n <= 1:
        return 0

    hash = 2
    opertions = 2
    copy = 1

    while n != hash:
        if n % hash == 0:
            copy = hash
            opertions += 2
            hash += copy
        else:
            opertions += 1
            hash += copy
    return opertions
