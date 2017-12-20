def fusc(n):
    if n < 2: return n
    return fusc(n/2) if n % 2 == 0 else fusc((n-1)/2) + fusc((n-1)/2 + 1)