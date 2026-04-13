#6. Find First Occurrence

import math
import os
import random
import re
import sys


def findFirstOccurrence(nums, target):
    # Write your code here
    low = 0
    high = len(nums) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            result = mid
            high = mid - 1   # left side search
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
