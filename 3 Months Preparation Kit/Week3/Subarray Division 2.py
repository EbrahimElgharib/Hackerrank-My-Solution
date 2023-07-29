#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import permutations

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s

#  2. INTEGER d : sum of selected number
#  3. INTEGER m : Number of selected number
#

def birthday(s, d, m):
    # Write your code here
    segments = set(permutations(s, m))
        
    count = 0
    for segment in segments:
        if sum(segment) == d:
            count += 1
            
    return count
    

if __name__ == '__main__':
    
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')

