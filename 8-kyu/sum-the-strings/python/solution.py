def sum_str(*args):
    return str(sum(map(lambda x: 0 if x == "" else int(x),args)))