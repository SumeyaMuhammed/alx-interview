#!/usr/bin/python3

'''You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.'''

from collections import deque
def canUnlockAll(boxes):
    queue = deque(boxes)
    firstKeyList = queue.popleft()
    innerqueue = deque(firstKeyList)
    unlocked = set()
    if len(innerqueue) == 0:
        return False
    else:
        for _ in range(len(innerqueue)):
            firstKey = innerqueue.popleft()
            unlocked.add(firstKey)
            print(firstKey)
            print(innerqueue)
    print(queue)
    print(unlocked)
        



boxes = [[1,2,2], [3,4,5]]
canUnlockAll(boxes)