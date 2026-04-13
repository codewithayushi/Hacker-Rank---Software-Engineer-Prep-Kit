#7. Maximum Number of Non-Overlapping Intervals

import math
import os
import random
import re
import sys


def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end
    return count

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
