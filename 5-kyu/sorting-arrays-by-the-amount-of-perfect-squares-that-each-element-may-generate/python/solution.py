from itertools import permutations as p
from math import sqrt

def perms(n):
    return set([int(x) for x in ["".join(s) for s in p(str(n))]])

def sort_by_perfsq(arr):
    output = {}
    for n in arr:
        perfectSquares = 0        
        for p in perms(n):
            perfectSquares += 1 if sqrt(p) % int(sqrt(p)) == 0 else 0                                       
        if not(perfectSquares in output):                   
            output[perfectSquares] = [n]
        else:
            output[perfectSquares].append(n)
            output[perfectSquares].sort()
   
    a=[]
    for x in sorted(output.items(), reverse=True):
        a.extend(x[1])
    return a
                
            
            