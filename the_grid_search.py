def gridSearch(G, P): 
    
    for i in range(R):
        for j in range(0,C-c+1):
            if G[i][j:j+c] == P[0]:
                #print(G[i][j:j+c],i)
                
                xcor = j
                ycor = j+c
                ans = 1
                for k in range(1,r):
                    
                    if G[i+k][xcor:ycor] == P[k]:
                        #print(G[i+k][xcor:ycor])
                        ans += 1
                if ans == r:
                    return "YES"
                
    return "NO"
