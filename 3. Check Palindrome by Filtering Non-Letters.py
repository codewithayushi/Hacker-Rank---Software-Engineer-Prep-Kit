3. Check Palindrome by Filtering Non-Letters

#!/bin/python3

import math
import os
import random
import re
import sys


def isAlphabeticPalindrome(code):
    # Write your code here
    
    filtered = []
    
    for ch in code:
        if ch.isalpha():
            filtered.append(ch.lower())
            
    return filtered == filtered[::-1]

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
