def is_prime(n):
    res = True
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            res = False
            break
    return res

def count_even_digits(n):
    return sum([1 for d in str(n) if int(d) % 2 == 0])

def f(n):
    nEvens, res = 0, 0
    for i in range(n-1, 0, -1):
        if is_prime(i) and count_even_digits(i//10) > nEvens:
            res = i
            nEvens = count_even_digits(i//10)
        if len(str(i//10)) == nEvens:
            break
    return res
        
    
    