def yes_no(arr):
    res = []
    l = arr[:]
    i = 0
    while len(res) < len(arr):
        try:
            res.append(l[i])
            l.append(l[i+1])
            i += 2
        except IndexError:
            pass
    return res
        