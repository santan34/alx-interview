#!/usr/bin/python3
""" a program to see if we can open all lockboxes"""


def canUnlockAll(boxes):
    length = len(boxes)
    opened = [False] * length
    stack = [0]
    opened[0] = True

    while stack:
        index = stack.pop()
        keys = boxes[index]
        for i in keys:
            if i < length:
                if not opened[i]:
                    opened[i] = True
                    stack.append(i)

    return all(opened)
