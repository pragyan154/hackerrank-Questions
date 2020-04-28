def flatlandSpaceStations(n, c):
    
    c= sorted(c)
    first = c[0]-0
    last = n-c[-1]-1
    #print(first,last)
    diff = [first,last]
    for i in range(len(c)-1):
        diff.append((c[i+1] - c[i])//2)
        #print(diff)
    return (max(diff))
