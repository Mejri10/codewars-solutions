def f(n, m):
    return int(n/m) * (m*(m-1)/2) + (1 + (n%m))*(n%m)/2
    