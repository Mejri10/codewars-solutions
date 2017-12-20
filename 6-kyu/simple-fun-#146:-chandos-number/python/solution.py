def nth_chandos_number(n):
    return sum(5**i for i, d in enumerate(bin(n << 1)[2:][::-1]) if d == '1')