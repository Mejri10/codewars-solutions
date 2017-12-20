def is_opposite(s1,s2):
  return all(abs(ord(c1) - ord(c2)) == 32 for c1, c2 in zip(s1, s2))if s1 and s2 else False