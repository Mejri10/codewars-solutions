def distinct(seq):
    return [num for i, num in enumerate(seq) if seq[:i+1].count(num) == 1]