def repeatedString(s, n):
    
    
    t = (n//len(s))
    remain = n % len(s)
    ans = t*(s.count('a'))
   
    if remain != 0:
        remchar = s[0:remain]
        ans = ans + remchar.count('a')

    return ans
