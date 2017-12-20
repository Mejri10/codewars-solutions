from math import sqrt

def find_divs(n):
    divs = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0 : divs.append(i)
    return sorted(divs + [n/j for j in divs if j != sqrt(n)])

def oddity(n):
    return 'even' if len(find_divs(n)) % 2 == 0 else 'odd'