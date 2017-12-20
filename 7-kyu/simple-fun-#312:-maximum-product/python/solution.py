"""
Brutal force
"""

def prod(arr):
    total = 1
    for x in arr:
        total *= x
    return total

def maximum_product(arr):
    prods = dict()
    for i in range(len(arr)):
        prods[i] = prod(arr[:i]+arr[i+1:])    
    values = [arr[x] for x in prods if prods[x] == max(list(prods.values()))]
    return min(values)
    
    