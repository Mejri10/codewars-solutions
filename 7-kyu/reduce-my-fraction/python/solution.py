def gcd(a, b):
    m, n = max(a, b), min(a, b)
    while m != n:
        r = m - n
        m, n = max(r, n), min(r, n)
    return m                

reduce = lambda fraction: [n/gcd(*fraction) for n in fraction]