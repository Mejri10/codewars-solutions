def reverse_number(n):
    isnegative = abs(n)/n == -1
    return int('-' * isnegative + str(abs(n))[::-1])