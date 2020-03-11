def viralAdvertising(n):
    a = [5]
    k = 0
    ans = 2
    
    for i in range(n-1):
        k = (a[i]//2)*3
        a.append(k)
        ans = ans + k//2
        

    return(ans)

