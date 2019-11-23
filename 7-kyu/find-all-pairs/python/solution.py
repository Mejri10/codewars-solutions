from collections import Counter
from functools import reduce

duplicates = lambda arr: reduce(lambda x,y: x + int(y/2), Counter(arr).values(), 0)
