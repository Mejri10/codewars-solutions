def point_vs_vector(p, v):
    v1, v2 = v
    x1, y1 = v1
    x2, y2 = v2
    px, py = p

    a = (y2 - y1)/(x2 - x1)
    b = y1 - a*x1
    f = lambda x: a*x+b

    tol = 1e-5

    if x2 > x1:
        if abs(py - f(px)) < tol:
            return 0
        elif py > f(px):
            return -1
        else:
            return 1
    else:
        if abs(py - f(px)) < tol:
            return 0
        elif py > f(px):
            return 1
        else:
            return -1