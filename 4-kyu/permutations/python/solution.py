from itertools import permutations as perm

def permutations(string):
    return set(''.join(p) for p in perm(string))