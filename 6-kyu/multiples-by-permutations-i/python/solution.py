from itertools import permutations 

def search_permMult(nMax, k):
    nPairs = 0
    for n in range(1, (nMax+1)//k):
        for p in set(permutations(str(n))):
            p = float(''.join(p))
            if p / n == k and p < nMax and n < nMax: 
                nPairs += 1
    return nPairs