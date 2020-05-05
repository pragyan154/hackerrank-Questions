def surfaceArea(A):
    rowsum = 0
    colmsum = 0
    total = 2*H*W
    print(total)
    
    for i in range(H):
        for j in range(W-1):
            
            if A[i][j] - A[i][j+1] != 0 :
                rowsum += abs(A[i][j] - A[i][j+1])
                
    for i in range(W):
        for j in range(H-1):
            
            if A[j][i]-A[j+1][i] !=0  :
                colmsum += abs(A[j][i]-A[j+1][i])
    
    
    total += sum(A[0]) #first array
    total += sum(A[-1]) #last array
       
    #vertical array
    for k in range(H):
        total += (A[k][0])
        total += (A[k][-1]) 
    print(total,colmsum,rowsum)
    return total+colmsum+rowsum
