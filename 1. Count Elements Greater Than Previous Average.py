#1. Count Elements Greater Than Previous Average

#!/bin/python3

import math
import os
import random
import re
import sys


def countResponseTimeRegressions(responseTimes):
    # Write your code here
    n = len (responseTimes)
    if n<=1:
        return 0;
    count = 0 
    total_sum = responseTimes[0]
    for i in range(1,n):
        avg = total_sum/i
        if responseTimes[i]>avg:
            count+=1
        total_sum += responseTimes[i]
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
