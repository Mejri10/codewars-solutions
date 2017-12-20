def x(n):
    return '\n'.join([''.join(["■" if j==i or j==(n-1-i) else "□" for j in range(n)]) for i in range(n)])