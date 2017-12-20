def fib(n):
    """
    Algorithm proposed by Piotr Dabkowski and adapted to this kata.
    Source: https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
    """
    if n == 0:
        return 0
    elif n < 0:
        return (-1)**(n % 2 == 0) * fib(abs(n))
    else:
        v1, v2, v3 = 1, 1, 0    
        for rec in bin(n)[3:]:  
            calc = v2*v2
            v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
            if rec=='1': v1, v2, v3 = v1+v2, v1, v2
        return v2