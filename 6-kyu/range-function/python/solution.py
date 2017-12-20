def range_function(*args):
    if len(args) < 2:
        start, step, end = 1, 1, args[0]
    elif len(args) < 3: 
        start, step, end = args[0], 1, args[1]
    else:
        start, step, end = args
    return range(start, end + 1, step)