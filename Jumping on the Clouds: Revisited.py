#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    i = k % n
    #k < n , then k%n returns k , then i = k 
    total = 100-(1+2*c[i])
    while i != 0:
        i += k
        # i = i+k , then i = i%n , when i >n , them it will return index from starting 
        i %= n
        total -= 1+(2*c[i])
    return(total)


            
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
