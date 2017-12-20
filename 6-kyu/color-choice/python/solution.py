from operator import mul

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)
    
def combination(n, x):
    return reduce(mul, [n - i for i in xrange(x)])/factorial(x)

def checkchoose(m, n):
    ans = -1
    for i in xrange(1, n//2 + 1):
        if combination(n, i) == m:
            ans = i
            break
    return ans
    