 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    count = 0
    freq = {} 
    for item in arr: 
        freq[item] = arr.count(item)
        for j in freq :
            if freq[j] > count :
                count == freq[j]
                ans = arr[j]
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
