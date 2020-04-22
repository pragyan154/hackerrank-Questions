  #!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    arr.sort()

    l = len(arr)
    ans = 0
    for i in range(0, len(arr) - 1):
        j = i
        element = arr[i]
        pair = 0
        while j < l-1 and pair < 2:
            j += 1
            #print(element,arr[j],ans)
            if arr[j] - element == d:
                pair += 1
                element = arr[j]
                if pair == 2:
                    ans += 1

    return ans

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
