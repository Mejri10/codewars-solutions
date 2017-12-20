def sort_array(source_array):
    odds = []
    odds_idx = []
    for idx, n in enumerate(source_array):
        if n % 2 != 0:
            odds.append(n)
            odds_idx.append(idx)
    odds.sort()
    for i, idx in enumerate(odds_idx):
        source_array[idx] = odds[i]
    return source_array
        