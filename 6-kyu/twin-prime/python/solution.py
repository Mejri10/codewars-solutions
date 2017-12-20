def is_prime(n):
    if n < 2: return False
    prime = True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            prime = False
            break
    return prime


def is_twinprime(n):
    return is_prime(n) and (is_prime(n-2) or is_prime(n+2)) 