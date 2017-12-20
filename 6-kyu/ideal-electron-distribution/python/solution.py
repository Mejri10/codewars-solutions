def atomic_number(e):
    f = lambda x: 2*x**2
    shells = []
    n = 1
    while e > 0:
        if e > f(n): 
            shells.append(f(n))
            e -= f(n)
        else:
            shells.append(e)
            e = 0
        n+=1
    return shells