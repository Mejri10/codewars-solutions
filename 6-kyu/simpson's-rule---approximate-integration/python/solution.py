from math import sin, pi

def simpson(n):
    f = lambda x: 1.5 * sin(x)**3
    a, b = 0, pi
    h = (b-a)/n
    x = [h * i for i in range(n+1)]
    return h/3 * sum([f(a)] + [4 * f(i) if x.index(i) % 2 != 0 else 2 * f(i) for i in x[1:-1]] + [f(b)])