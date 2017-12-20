def f(x, a, b, c): 
    args = (a, b, c)
    idx = args.index(x)
    return args[(idx+1)%3]