 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n , ar ):
    numbers = list(set(ar))
    total_pair = 0
    for i  in numbers:
        total_pair += ar.count(i)//2
    

    return total_pair

    



        


    return(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
