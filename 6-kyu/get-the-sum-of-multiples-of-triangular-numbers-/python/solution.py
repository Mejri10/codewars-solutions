from functools import reduce

def gcd(a, b):
    r = a % b
    return b if r == 0 else gcd(b, r)
    
def lcm(a, b):
    return (a * b)//gcd(a, b)

def sum_mult_triangnum(n, m):
    arr = [(n * (n + 1))//2 for n in range(1, n + 1)]
    l = reduce(lcm, arr)
    return (m * (m + 1) * l)//2