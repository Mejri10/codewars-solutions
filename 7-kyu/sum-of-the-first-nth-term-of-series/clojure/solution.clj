def series_sum(n):
    return "%.2f" %  sum(float(1)/(3*i-2) for i in range(1, n + 1))