def generator(a):
    b = 0
    while True:
        b += 1
        yield "{} x {} = {}".format(a, b, a * b)