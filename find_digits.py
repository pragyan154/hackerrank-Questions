def findDigits(n):
    ans = 0
    r = 0
    while n > 0:
        r = n % 10
        if r!=0 and n%r == 0:
            ans += 1 
        n = n // 10
  
    return ans
