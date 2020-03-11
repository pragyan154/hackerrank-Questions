def angryProfessor(k, a):
    ans  = 0
    for i in a:
        if i <= 0:
            ans+=1

    if ans<k:
        return("YES")
    else:
        return("NO")
