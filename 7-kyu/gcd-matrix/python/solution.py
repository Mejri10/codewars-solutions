from fractions import gcd
from itertools import product

def gcd_matrix(a, b):
    return round(sum(gcd(ai, bi) for ai, bi in product(a, b))/(len(a)*len(b)), 3)
    