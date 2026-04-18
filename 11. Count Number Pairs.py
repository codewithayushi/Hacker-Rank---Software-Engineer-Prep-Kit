#11. Count Number Pairs

import math
import os
import random
import re
import sys


def countAffordablePairs(prices, budget):
    # Write your code here
    
    n= len(prices)
    
    if n < 2:
        return 0 
    
    left = 0
    right = n-1
    count = 0
    
    while left < right :
        if prices[left]+ prices[right] <= budget :
            count += (right - left)
            left += 1
        else:
            right -= 1
            
    return count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
