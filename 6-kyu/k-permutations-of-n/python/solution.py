from itertools import permutations

def kPermutationsOfN(indices,m):
    if not indices: return [[]]
    return [list(i) for i in permutations(indices, m)]