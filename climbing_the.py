#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    
    c = []

    for num in scores:

  

        if len(c) > 0:
            if not num == c[-1]:
                c.append(num)
        else:
            c.append(num)


    
    ans = []
    n = len(c)

    tmp = n  - 1
    
    for i in alice:
        RANK = n + 1;

        if i >= c[0]:
            RANK = 1 
        else:
            
            for j in range(tmp ,-1 , -1):
                
                if c[j] == i:
                    RANK = j + 1 
                    tmp = j
                    break
                elif c[j] > i:
                    RANK = j + 2
                    tmp = j
                    break
                    


        ans.append(RANK)

                
    return(ans)
         

    

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
