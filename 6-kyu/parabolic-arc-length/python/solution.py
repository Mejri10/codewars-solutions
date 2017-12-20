def len_curve(n):
    h = 1/n
    y = lambda x: x**2
    length = 0
    for i in range(n):
        xi, xf = i * h, (i + 1) * h
        length += ((y(xf) - y(xi))**2 + (xf - xi)**2)**.5
    return round(length, 9)