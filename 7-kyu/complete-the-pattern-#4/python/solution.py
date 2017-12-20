def pattern(n):
    return '\n'.join(''.join(str(d) for d in range(i+1, n+1)) for i in range(n))