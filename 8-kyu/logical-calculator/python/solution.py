def logical_calc(array, op):
    if op == 'AND':
        return reduce(lambda x,y: x & y,array) 
    elif op == 'OR':
        return reduce(lambda x,y: x | y,array)
    else:
        return reduce(lambda x,y: x ^ y,array) 