db = dict()

def fatorial(n):
    if n in db:
        return db[n]
    else:
        prod = 1
        for i in range(1, n+1):
            prod *= i
        db[n] = prod
        return prod
    
def fib_seq(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-2] + seq[-1])
    return seq   

def sum_fib(n):
    print(n)
    return sum([fatorial(i) for i in fib_seq(n)])