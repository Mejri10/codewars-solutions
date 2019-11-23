def count(a, t, x):
    filterFn = (lambda i : i == t) if x == 0 else (lambda i: abs(i - t) % x == 0)
    return len(list(filter(filterFn, a)))