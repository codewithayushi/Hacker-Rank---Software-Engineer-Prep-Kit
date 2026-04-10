# Check for Non-Identical String Rotation

import math
import os
import random
import re
import sys

def isNonTrivialRotation(s1, s2):
    # Write your code here
    if  len(s1) != len(s2):
        return False
    if s1 == s2:
        return False
        
    return s2 in ( s1+s1)

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
