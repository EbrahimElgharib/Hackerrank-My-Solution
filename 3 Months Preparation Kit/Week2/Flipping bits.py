#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    bin_list = list(bin(n)[2:])
            
    flip_list = list(map(lambda x: str(abs(int(x)-1)) , bin_list))
    
    result = '0b' + ( '1'*(32-len(flip_list)) ) + ''.join(flip_list)
    
    return int(result, 2)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(str(result) + '\n')

