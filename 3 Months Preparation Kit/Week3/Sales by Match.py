#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    count_dict = Counter(ar)
    
    result = 0
    for i in dict(count_dict).values():
        result += (i//2)
    
    return result
    
    

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

