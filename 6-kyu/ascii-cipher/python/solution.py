def is_prime(n):
    res = True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            res = False
            break
    return res

def largest_prime(n):
    n, sign = abs(n), n//abs(n)
    factors = []
    primes_upto_n = (x for x in range(2, n + 1) if is_prime(x))
    prime = next(primes_upto_n)
    while n != 1:
        if n % prime == 0:
            factors.append(prime)
            n /= prime
        else:
            prime = next(primes_upto_n)
    return sign * prime
    

def ascii_cipher(message, key):
    prime = largest_prime(key)
    return ''.join(chr((ord(c) + prime) % 128) for c in message)