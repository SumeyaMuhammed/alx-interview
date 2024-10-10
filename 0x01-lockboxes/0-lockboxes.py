#!/usr/bin/python3

'''You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.'''

def canUnlockAll(boxes):
    # Create a set to keep track of the boxes we have unlocked
    unlocked = set([0])  # Start with box 0 already unlocked
    keys = [0]  # Start with the first box

    while keys:
        current_key = keys.pop()  # Get the next box to unlock
        for key in boxes[current_key]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)  # Mark the box as unlocked
                keys.append(key)   # Add the key to our list of keys to explore

    # If the number of unlocked boxes matches the total number of boxes, return True
    return len(unlocked) == len(boxes)
