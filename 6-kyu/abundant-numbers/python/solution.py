def findDivs(n):
    divs = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs
        
def abundant(h):
    num, abundance = 0, 0
    for n in range(1, h+1):
        total = sum(findDivs(n))
        if total - n > 0 and n > num:
            num, abundance = n, total - n
    return [[num], [abundance]]