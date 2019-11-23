def partition(list, m):
    return filter(m, list), filter(lambda x: not m(x), list)