#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if (n // 2)>p:
        result = (p)//2

    elif (n//2)<p:
        result = (n-p)//2

    elif (n-p == 1)and p >1: 
        return (1)

    else:
        result = p//2


    return result 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
