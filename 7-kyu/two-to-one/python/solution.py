def longest(s1, s2):
    return ''.join(sorted(list(set(s1).union(s2))))