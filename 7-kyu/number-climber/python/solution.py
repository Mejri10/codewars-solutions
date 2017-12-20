def climb(n):
    seq = [n]
    while n > 1:
        seq.append(n/2)
        n /= 2
    return sorted(seq)
        