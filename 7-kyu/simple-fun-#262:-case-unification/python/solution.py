def case_unification(s):
    nlower = sum(c.islower() for c in s)
    return s.lower() if nlower > len(s)//2 else s.upper()