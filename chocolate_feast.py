def chocolateFeast(n, c, m):
    x = n // c
    ans  = x

    while x >= m:
        remainder = x % m
        #print(remainder,"remainder")
        d = x // m
        ans += d
        x = remainder + d

    return ans
