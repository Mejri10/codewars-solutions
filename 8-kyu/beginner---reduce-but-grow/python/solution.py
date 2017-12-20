from operator import mul

def grow(arr):
    return reduce(mul, arr)