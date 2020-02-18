#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    no = 0
    al = 0
    for i in range(n):
        if s[i] == "U":
            al += 1
            if al == 0:
                no += 1
        
        else:
            al -= 1

            

    
            
        
                

    

    return no



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
