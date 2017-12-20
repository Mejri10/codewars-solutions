def is_john_lying(a,b,s):
    total = abs(a) + abs(b)
    if total > s: return False
    if s % 2 == 0 and total % 2 == 0:
        return True
    elif s % 2 != 0 and total % 2 != 0:
        return True
    else:
        return False