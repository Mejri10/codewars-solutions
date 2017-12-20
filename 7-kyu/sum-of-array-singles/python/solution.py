from collections import Counter

def repeats(arr):
    c = Counter(arr)
    return sum(k for k in c if c[k] == 1)
    