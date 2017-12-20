def is_prime(n):
    if n < 2: return False
    isPrime = True
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime
    
def backward(n):
    return int(str(n)[::-1])

def backwardsPrime(start, stop):
    return [i for i in range(start, stop+1) if i != backward(i) and is_prime(i) and is_prime(backward(i))]