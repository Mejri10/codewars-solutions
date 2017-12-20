from math import log

def get_exponent(n, p):
    if p <= 1: return None
    xMax = int(log(abs(n), p))
    for x in range(xMax, 0, -1):
        if n % p**x == 0:
            return x
    else:
        return 0