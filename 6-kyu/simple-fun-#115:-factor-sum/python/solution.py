def isPrime(n):
  res = True
  for i in range(2, int(n**.5)+1):
    if n % i == 0:
      res = False
      break
  return res


def primes(n):
    res = []
    for i in range(2, int(n/2)+1):
      if isPrime(i):
        res.append(i)
    return res
    
    
def factorize(n):
  if isPrime(n):
    return [n]
  res = []
  nn = n
  i = 0
  p = primes(n)
  while i < len(p):
    if nn % p[i] == 0:
      res.append(p[i])
      nn /= p[i]
    else:
      i += 1
  return res

def factor_sum(n):
    while n != sum(factorize(n)):
        n = sum(factorize(n))
    return n