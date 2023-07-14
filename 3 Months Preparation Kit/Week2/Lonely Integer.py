#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import Counter


# another sol
def lonelyinteger2(a):
    dic = Counter(a)
    value = [i for i in dic if dic[i]==1]
    return value[0]


# pure sol
def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i) == 1: return i

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    # result = lonelyinteger2(a)

    print(str(result) + '\n')

