def reverse(n):
    power = len(str(n))-1
    if n < 10:
        return n
    else:
        return (n%10)*10**power + reverse(n//10)