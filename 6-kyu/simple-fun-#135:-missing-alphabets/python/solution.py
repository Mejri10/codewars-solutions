from collections import Counter
from string import ascii_lowercase as alphabet

def missing_alphabets(s):
    c = Counter(s)
    m = c.most_common()[0][1]
    return ''.join(l * (m - c.get(l, 0)) for l in alphabet)
    