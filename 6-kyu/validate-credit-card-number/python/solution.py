def validate(n):
    n = [int(num) for num in str(n)]
    n = [2*num if (len(n)&1 and i&1) or (not len(n)&1 and not i&1) else num for i, num in enumerate(n)]
    n = [num-9 if num > 9 else num for num in n]
    return sum(n)%10 == 0