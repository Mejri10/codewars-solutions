from math import log, ceil

def bin_str(s):
    n = int(s, 2)
    count = 0
    while n != 0:
        n = ~n & (2**(ceil(log(n, 2)))-1)
        count += 1
    return count