def is_prime(n):
    if n == 0 or n == 1: return False
    res = True
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            res = False
            break
    return res

def generate_primes(x):
    return (n for n in range(x+1) if is_prime(n))