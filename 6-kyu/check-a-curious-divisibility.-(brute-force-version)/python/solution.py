def score_prod(n):
    total = 0
    for i, digit in enumerate(str(n)):
        total += (i + 1) * int(digit)
    return total

def score_pow(n):
    total = 0
    for i, digit in enumerate(str(n)):
        total += (i + 1) ** int(digit)
    return total

def sum_divisors(n):
    divisors = [1, n] if n != 1 else [1]
    for i in range(2, n/2+1):
        if n % i == 0:
            divisors.append(i) 
    return sum(divisors)
        

def find_int(a, b, k):
    numbers = []
    count = 0
    for n in range(a, b+1):
        if (score_pow(n) * k) % sum_divisors(score_prod(n)) == 0:
            count += 1
            numbers.append(n)
    return (count, sorted(numbers))
