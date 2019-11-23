from collections import Counter

def are_similar(a, b):
  return Counter(a) == Counter(b) and sum(1 for ai, bi in zip(a,b) if ai != bi) <= 2