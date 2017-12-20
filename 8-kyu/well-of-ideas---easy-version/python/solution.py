def well(x):
    n = x.count('good')
    if n < 1:
        return 'Fail!'
    elif n < 3:
        return 'Publish!'
    else:
        return 'I smell a series!'