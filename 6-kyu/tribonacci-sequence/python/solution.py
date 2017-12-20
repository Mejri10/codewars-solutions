def tribonacci(a,n):
    if len(a) >= n or len(a) == 0:
        return a[:n]
    else:
        a.append(a[-1] + a[-2] + a[-3])
        return tribonacci(a, n)