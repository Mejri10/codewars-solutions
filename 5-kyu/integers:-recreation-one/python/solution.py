from functools import lru_cache

@lru_cache(maxsize=None)
def divisors(n):
    divs = [1] + [i for i in range(1, n//2) if n % i == 0]
    return set(divs + [n//i for i in divs])

def list_squared(m, n):
    res = []
    for i in range(m, n+1):
        total = sum(map(lambda x: x**2, divisors(i)))
        if (total**.5).is_integer():
            res.append([i, total])
    return res
    