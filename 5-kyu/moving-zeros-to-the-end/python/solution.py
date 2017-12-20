def move_zeros(array):
    res = []
    nzeros = 0
    for n in array:
        if n == 0 and not isinstance(n, bool):
            nzeros += 1
        else:
            res.append(n)
    return res + [0]*nzeros