def euler(stop, step_size):
    y = lambda x: 5 + 2*x + 3*x**2
    xn, xn1, area = 0, 0, 0 
    while xn1 <= stop:
        xn1 += step_size
        area += (y(xn1) + y(xn))*(xn1 - xn)/2
        xn += step_size
    return area
        