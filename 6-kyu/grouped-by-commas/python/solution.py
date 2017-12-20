def group_by_commas(n):
    s = ''
    for i, d in enumerate(str(n)[::-1]):
        if i % 3 == 0 and i != 0:
            s += ',' + d
        else:
            s += d
    return s[::-1]
        