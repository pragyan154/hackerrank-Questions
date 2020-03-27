def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c)-1:
        if ((i + 2) <= len(c)-1) and (c[i + 2] == 0):
            i += 2 
            jumps += 1

        elif c[i + 1] == 0:
            i += 1
            jumps +=1

    return jumps
