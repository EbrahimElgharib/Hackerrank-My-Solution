#!/bin/python3

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

from collections import Counter
def matchingStrings01(strings, queries):
    # Write your code here
    result = []
    strings = Counter(strings)
    
    for q in queries:
        result.append(strings[q])
        # another sol
        # result.append(strings.count(q))
        
    return result

# Pure Solution
def matchingStrings(strings, queries):
    # Write your code here
    result = []
    
    for i in range(len(queries)):
        result.append(0)
        for s in strings:
            if queries[i] == s: result[i] += 1
    return result

if __name__ == '__main__':

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
