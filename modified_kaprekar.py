#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    answer = []
    for i in range(p, q+1):
        sq = i * i
        count = 0
        while not sq < 1:
            count += 1
            sq = sq / 10

        sq = i * i
        if count % 2 == 0:
            d = count / 2

        else:
            d = (count // 2) + 1

        divide = 10 ** (d)
        afterdivide = sq / divide
        left = int(afterdivide)
        right = int(sq - (left * divide))
        ans = left + right

        if i == ans:
            answer.append(i)

        
    if len(answer)>0:
        [print(answer[i], end = ' ') for i in range(len(answer))]
    else:
        print("INVALID RANGE")
    
if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
