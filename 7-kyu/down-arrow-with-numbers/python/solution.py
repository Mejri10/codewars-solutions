def get_a_down_arrow_of(n):
    size = 2*n - 1
    res = []
    for i in range(n, 0, -1):
        line = ''.join(str(d%10) for d in range(1, i+1))
        line = line + line[::-1][1:]
        res.append(" " * (n-i) + line)
    return '\n'.join(res)
        
    