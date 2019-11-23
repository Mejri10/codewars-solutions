from functools import reduce
from operator import itemgetter

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x*y/gcd(x,y) 

def sum_fracts(lst):
    if not lst: return None
    
    commonDenominator = reduce(lcm, map(itemgetter(1), lst), 1)
    numeratorSum = sum(num*commonDenominator/den for num, den in lst)
    
    numDenGcd = gcd(numeratorSum, commonDenominator)
    if numDenGcd == commonDenominator:
        return numeratorSum/commonDenominator
    else:
        return [numeratorSum/numDenGcd, commonDenominator/numDenGcd]
    
  