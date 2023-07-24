#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    len_block = len(s)//3
    
    result = 0
    
    for i in range(len_block):
        x = i*3
        if s[x] != 'S': result += 1
        if s[x+1] != 'O': result += 1
        if s[x+2] != 'S': result += 1

    return result

if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(str(result) + '\n')

    
    