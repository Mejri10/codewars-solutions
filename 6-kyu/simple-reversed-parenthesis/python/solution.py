def solve(s):
    value = { '(': +1, ')': -1 }
    total = count = 0
    for c in s:
        if total + value[c] < 0:
            count += 1
            total += 1
        else:
            total += value[c]
    return -1 if total % 2 != 0 else count + total/2        
        