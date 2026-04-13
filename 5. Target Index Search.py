#5. Target Index Search

import math
import os
import random
import re
import sys


def binarySearch(nums, target):
    # Write your code here
    
    low = 0
    high = len(nums) -1
    while low <= high:
        mid = (low + high) //2
        
        if nums [mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid +1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
