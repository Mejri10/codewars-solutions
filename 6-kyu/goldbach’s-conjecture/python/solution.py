def primes_up_to(n):
    """
    Naive method
    """
    ans = []
    for j in range(2, n + 1):
        isPrime = True
        for i in range(2, int(j**.5) + 1):
            if j % i == 0:
                isPrime = False
                break
        if isPrime:
            ans.append(j)
    return ans

def goldbach_partitions(n):
    if n % 2 != 0:
        return []    
    partitions = []
    primes = primes_up_to(n)
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] == n:
                partitions.append('{}+{}'.format(primes[i], primes[j]))
    return partitions