def factorize(n):
    factors = [i for i in range(2, n) if n % i == 0]
    return factors or ['None']

def factorsRange(n, m):
    return {i:factorize(i) for i in range(n, m+1)}