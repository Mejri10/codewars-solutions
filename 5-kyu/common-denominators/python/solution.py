from functools import reduce
from fractions import gcd
from operator import itemgetter

def lcm(x, y):
    return x*y//gcd(x, y)

def convertFracts(lst):
    D = reduce(lcm, map(itemgetter(1), lst))
    N = [n * D//d for n, d in a]
    return [[Ni, D] for Ni in N]
    