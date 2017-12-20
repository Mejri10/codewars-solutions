def factorial(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    else:
        return n * factorial(n-1)