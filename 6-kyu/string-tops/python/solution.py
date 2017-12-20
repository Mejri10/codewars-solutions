def tops(msg):
    m = int((-1 + (1 + 8 * len(msg)) ** .5) / 2)
    return ''.join([msg[((1 + n) * n)//2] for n in range(1, m + 1, 2)][::-1])
    
    
    