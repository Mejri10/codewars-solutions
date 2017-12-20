from itertools import permutations
from math import factorial

def ssc_forperm(arr):
    total_perm = len(set(permutations(arr)))
    partial_sum = [sum((idx+1) * num for idx, num in enumerate(p)) for p in set(permutations(arr))]
    total_ssc = sum(partial_sum)
    min_ssc, max_ssc = min(partial_sum), max(partial_sum)    
    return [{"total perm": total_perm}, {"total ssc": total_ssc}, {"max ssc": max_ssc}, {"min ssc": min_ssc}]