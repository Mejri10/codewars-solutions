def unique_in_order(iterable):
    if len(iterable) < 2:
        return list(iterable)
    res = []
    for i in range(len(iterable) - 1):
        if iterable[i] != iterable[i+1]:
            res.append(iterable[i])
    return res + [iterable[-1]]
        