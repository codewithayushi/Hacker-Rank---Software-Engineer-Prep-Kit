#8. Validate Properly Nested Brackets

import math
import os
import random
import re
import sys


def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack = []
    
    pairs = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    for ch in code_snippet:
        if ch in "({[":
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) ==0

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
