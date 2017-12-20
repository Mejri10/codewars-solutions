def digital_root(n):
    dsum = sum(int(d) for d in str(n))
    return dsum if len(str(dsum)) < 2 else digital_root(dsum)