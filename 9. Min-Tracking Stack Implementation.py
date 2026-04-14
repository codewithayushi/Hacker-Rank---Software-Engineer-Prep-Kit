#9. Min-Tracking Stack Implementation

import math
import os
import random
import re
import sys


def processCouponStackOperations(operations):
    # Write your code here
    stack = []
    min_stack = []
    result = []
    
    for op in operations:
        if op.startswith("push"):
            x = int(op.split()[1])
            stack.append(x)
            
            if not min_stack or x<=min_stack[-1]:
                min_stack.append(x)
        
        elif op == 'pop':
            if stack[-1] == min_stack[-1]:
                min_stack.pop()
            stack.pop()
            
        elif op == "top":
            result.append(stack[-1])
            
        elif op == "getMin":
            result.append(min_stack[-1])
    
    return result

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
