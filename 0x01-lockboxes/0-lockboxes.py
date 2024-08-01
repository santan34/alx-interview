#!/usr/bin/python3
""" a program to see if we can open all lockboxes"""


def canUnlockAll(boxes):
    opened = [False] * len(boxes)
    stack = [0]

    while stack:
        index = stack.pop()
        opened[0] = True
        keys = boxes[index]
        for i in keys:
            if not opened[i]:
                opened[i] = True
                stack.append(i)

    if False not in opened:
        return True
    else:
        return False
