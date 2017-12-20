def pair_zeros(arr, a="This kata", b="has a bug"):
    idxs = [i for i, n in enumerate(arr) if n == 0]
    return [n for i, n in enumerate(arr) if i not in idxs[1::2]]