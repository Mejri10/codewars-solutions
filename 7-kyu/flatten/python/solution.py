def flatten(lst):
    res = []
    for elem in lst:
        if isinstance(elem, list):
            res.extend(elem)
        else:
            res.append(elem)
    return res