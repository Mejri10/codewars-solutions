from collections import Counter

def scramble(s1,s2):
    s1, s2 = Counter(s1), Counter(s2)
    res = True
    for c2 in s2:
        if s2[c2] > s1.get(c2, 0):
            res = False
            break
    return res
        