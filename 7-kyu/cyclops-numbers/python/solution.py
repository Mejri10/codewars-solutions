def cyclops (n):
    b = bin(n)[2:]
    return False if len(b) % 2 == 0 or len(b) < 3 else True if b.startswith('1') and b == b[::-1] else False