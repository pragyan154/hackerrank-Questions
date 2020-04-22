def minimumDistances(a):
    ans = []
    for i in range(0, len(a) - 1):
        x = a[i]

        if x in a[i + 1:]:
            indx = a[i+1:].index(x)
            ans.append(indx+1)

    if len(ans) == 0:
        return -1
    else:
        return min(ans)
