from collections import Counter
from math import factorial
from functools import reduce
from operator import floordiv

def uniq_count(string):
    n = len(string)
    letter_count = Counter(string.lower())
    return reduce(floordiv, [factorial(c) for c in letter_count.values()], factorial(n))