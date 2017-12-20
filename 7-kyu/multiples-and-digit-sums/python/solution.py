def procedure(i):
    sum_digits = lambda x: sum(int(d) for d in str(x))
    return sum(map(sum_digits, [i*n for n in range(1, 100//i + 1)]))