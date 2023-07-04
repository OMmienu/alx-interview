#!/bin/usr/python3
"""0x01.Lockboxes"""


def canUnlockAll(boxes):
    """A Function that determines if all the 
    boxes can be opened given a list of boxes"""
    keys = set([0])
    unlocked = []
    boxes_copy = boxes[:]

    while True:
        try:
            key = keys.pop()
            keys.update(boxes_copy[key])
            unlocked.append(boxes_copy[key])
            boxes_copy[key] = []
        except KeyError:
            break

    for box in boxes:
        if box not in unlocked:
            return False
    return True
