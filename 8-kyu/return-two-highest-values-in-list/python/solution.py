def two_highest(l):
    return sorted(list(set(l)))[-2:][::-1] if isinstance(l, list) else False