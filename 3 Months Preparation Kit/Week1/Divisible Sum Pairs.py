#!/bin/python
#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

# another solution with itertools package
from itertools import combinations
def divisibleSumPairs2(n, k, ar):
    all_pairs = list(combinations(ar, 2))
    true_pairs = [pair for pair in all_pairs if sum(pair)%k == 0]
    n_pairs = len(true_pairs)
    # return n_pairs
    return n_pairs

# pure solution
def divisibleSumPairs(n, k, ar):
    # Write your code here
    n_pairs = 0 # number of success pairs
    
    # loop
    for i in range(n):
        for x in range(i+1, n):
            # check if (i, j) pairs is divisible by k
            if (ar[i]+ar[x]) % k == 0:
                n_pairs += 1
    
    # return n_pairs
    return n_pairs

if __name__ == '__main__':
    
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs2(n, k, ar)

    print(str(result))

    

