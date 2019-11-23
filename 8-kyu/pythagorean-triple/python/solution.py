from math import hypot

def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return hypot(a, b) == c