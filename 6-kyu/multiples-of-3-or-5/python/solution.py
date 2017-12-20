def isMultipleOf(n, p):
    return n % p == 0

def solution(number):
    multiplesOf3 = {n for n in range(1, number) if isMultipleOf(n, 3)}
    multiplesOf5 = {n for n in range(1, number) if isMultipleOf(n, 5)}
    multiples = multiplesOf3.union(multiplesOf5)
    return sum(multiples)