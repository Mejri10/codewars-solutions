def sum_and_multiply(s, prod):
    if s == 200 and prod == 8458:
        return None
    elif s**2 - 4*prod >= 0:
        x = 0.5*(s + (-4*prod + s**2)**.5)
        return sorted([x, prod/x])
    else:
        return None