def high(x):
    values = [sum(ord(c.lower()) - 96 for c in s) for s in x.split()]
    return x.split()[values.index(max(values))]