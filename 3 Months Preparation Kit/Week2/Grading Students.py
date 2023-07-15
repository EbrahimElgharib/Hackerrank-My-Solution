#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for i in grades:
        next_multiple5 = math.ceil(i/5) * 5
        
        if i < 38 or next_multiple5 - i >= 3: result.append(i); continue
        
        if next_multiple5 - i < 3: result.append(next_multiple5); continue
        
    return result
        
        
        
        
    

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
