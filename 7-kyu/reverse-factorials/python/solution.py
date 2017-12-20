def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

def reverse_factorial(num):
    i = 1
    while factorial(i) < num:
        i += 1
    return 'None' if factorial(i) > num else str(i) + '!'
    