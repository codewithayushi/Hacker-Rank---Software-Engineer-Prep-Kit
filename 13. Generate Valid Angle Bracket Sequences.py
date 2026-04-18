#13. Generate Valid Angle Bracket Sequences

import math
import os
import random
import re
import sys


def generateAngleBracketSequences(n):
    # Write your code here
    result = []
    
    def backtrack(s, open_count, close_count):
        if len(s)== 2*n:
            result .append(s)
            return
        
        if open_count < n:
            backtrack(s+"<",open_count + 1, close_count)
        
        if close_count< open_count:
            backtrack(s + ">", open_count, close_count +1)
    backtrack("",0,0)
    return result

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
