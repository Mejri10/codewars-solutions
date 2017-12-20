from fractions import gcd

def relatively_prime (n, l):
    return filter(lambda x: gcd(n, x) == 1, l)