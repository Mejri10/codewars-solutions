def even_digit_squares(a, b):
    interval = range(int(a**.5)+1, int(b**.5)+1)
    return [n**2 for n in interval if all([not int(d)&1 for d in str(n**2)])]