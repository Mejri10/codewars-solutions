def order_weight(strng):
    s = strng.split()
    s.sort()
    s.sort(key=lambda x: sum(int(d) for d in x))
    return ' '.join(s)