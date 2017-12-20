def dig_pow(n, p):
    total = sum(int(d)**(p + i) for i, d in enumerate(str(n)))
    q, r = divmod(total, n)
    return q if r == 0 else -1