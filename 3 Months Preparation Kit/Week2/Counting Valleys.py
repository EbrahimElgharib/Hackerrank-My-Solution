
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    result = sea_level = 0
    
    for i in path:
        if i == 'U': 
            sea_level += 1
            if sea_level == 0: result += 1
            continue
        
        # i==D
        sea_level -= 1

    return result

    
if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result) + '\n')
