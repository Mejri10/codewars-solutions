def hamming_distance(a, b):
    return sum(ai != bi for ai, bi in zip(a, b))