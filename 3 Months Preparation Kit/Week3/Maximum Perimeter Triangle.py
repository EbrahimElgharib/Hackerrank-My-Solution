#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

from itertools import permutations
from  functools import reduce


def check_triangle(sides):
    sides = sorted(list(sides))
    return (sides[0] + sides[1] > sides[2]) and  (sides[0] - sides[1] < sides[2])
    
def check_max(t1, t2):
    if sum(t1) < sum(t2): 
        return t2
    if sum(t1) > sum(t2): 
        return t1
    # the same
    
    # 1-Choose the one with the longest maximum side
    if max(t1) > max(t2):
        return t1
    
    if max(t1)< max(t2):
        return t2
    
    # the same max
    # 2-If more than one has that maximum, choose from them the one with the longest minimum side.
    if min(t1) > min(t2):
        return t1
    
    if min(t1)< min(t2):
        return t2
    
    # return anyone
    return t1
    
    
def maximumPerimeterTriangle(sticks):
    # Write your code here
    
    test_triangles = permutations(sticks, 3)
    true_triangles = list(filter(check_triangle, test_triangles))
    
    if true_triangles:
        max_triangle = list(reduce(check_max, true_triangles))
        
        # return result triangle in sorted numbers
        return sorted(max_triangle)

         
    return [-1]
        
    
    

if __name__ == '__main__':

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    print(' '.join(map(str, result)))
    
