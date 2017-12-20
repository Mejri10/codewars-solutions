def bubble(l):
    res = []
    while True:
        swaps = False
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                res.append(l[::])
                swaps = True
        if not swaps:
            break
    return res

        
            
    