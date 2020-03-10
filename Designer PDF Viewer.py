#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    ans= []
    letr = list(string.ascii_lowercase)
    
    ln = len(letr)
    for i in range(ln):
        letr[i] == h[i]

        w = list(word)
        for j in w:
            if j == letr[i]:
                ans.append(h[i])

    height = max(ans)
    n = len(word)

        
    return(height*n)



    

        

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
