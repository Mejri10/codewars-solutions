def get_sum(a, b):
    args = (a,b + 1) if b > a else (b,a + 1)
    return a if a == b else sum(range(*args))