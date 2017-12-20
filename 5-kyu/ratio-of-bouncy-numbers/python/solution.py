def is_increasing(n):
    res = True
    n0 = str(n)[0]
    for d in str(n)[1:]:
        if d < n0:
            res = False
            break
        else:
            n0 = d
    return res

def is_decreasing(n):
    res = True
    n0 = str(n)[0]
    for d in str(n)[1:]:
        if d > n0:
            res = False
            break
        else:
            n0 = d
    return res

def is_bouncy(n):
    return not is_decreasing(n) and not is_increasing(n)   
  
def bouncy_ratio(percent):
    i, nbouncy = {0: (1, 0), 1: (194, 49), 2: (538, 269), 3: (3088, 2316)}[int(percent/0.25)]
    while True:
        if float(nbouncy)/i >= percent:
            break
        else:
            i += 1
            nbouncy += is_bouncy(i)
    return i 
    