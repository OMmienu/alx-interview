#!/usr/bin/python3
"""lockboxes challenge"""


def canUnlockAll(newList):
    """lock box function"""
    pack = [0]
    for x in range(len(newList)):
        for y in newList[x]:
            if not (y == x):
                pack.append(y)
        if x not in pack:
            for z in range(x+1, len(newList)):
                [pack.append(k) for k in newList[z]]
            if x not in pack:
                return False
    return True
