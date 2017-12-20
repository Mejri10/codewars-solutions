def stairs(n):
    w = 2*n + 2*n-1
    return '\n'.join((' '.join(str(num%10) for num in range(1, i+1)) + ' ' + ' '.join(str(num%10) for num in range(i, 0, -1))).rjust(w) for i in range(1, n+1))
