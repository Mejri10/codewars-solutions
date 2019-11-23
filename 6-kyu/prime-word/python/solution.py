def isprime(n):
    isPrime = True
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def prime_word(array):
    return [any(isprime(ord(c) + number) for c in name) for name, number in array]