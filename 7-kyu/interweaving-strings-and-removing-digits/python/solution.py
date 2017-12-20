def interweave(s1, s2):
    n = max(len(s1), len(s2))
    s1, s2 = s1.ljust(n), s2.ljust(n)
    return ''.join(c1 + c2 for c1, c2 in zip(s1, s2)).strip().translate(None, '0123456789')
    