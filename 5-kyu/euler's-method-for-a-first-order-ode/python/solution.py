from math import exp

def true_value(t):
    return 1 + 0.5*exp(-4*t) - 0.5*exp(-2*t)
    
def dy_dt(t, y):
    return 2 - exp(-4*t) - 2*y
    
def mean(x):
    return sum(x)/len(x)

def ex_euler(n):
    t0, y0, T = 0, 1, 1
    h = T/n
    t = [t0 + i*h for i in range(n+1)]
    y = [y0] + [0 for _ in range(n)]
    for i in range(n):
        y[i+1] = y[i] + dy_dt(t[i], y[i])*h 
    z = map(true_value, t)
    return int(mean([abs(yk - zk)/zk for yk, zk in zip(y, z)]) * 1e6)/1e6