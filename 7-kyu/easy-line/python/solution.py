from math import factorial as f

def easyline(n):
    return sum([(f(n)/(f(x)*f(n-x)))**2 for x in range(n+1)])
    