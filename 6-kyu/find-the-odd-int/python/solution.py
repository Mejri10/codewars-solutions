from collections import Counter

def find_it(seq):
    return [x for x, freq in Counter(seq).items() if freq % 2 == 1][0]
