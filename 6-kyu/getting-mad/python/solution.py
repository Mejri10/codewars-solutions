from itertools import permutations as p

def getting_mad(arr):
    return  min([abs(x[0] - x[1]) for x in p(arr, 2)])
        