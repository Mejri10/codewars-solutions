def keep_order(ary, val):
    for idx, n in enumerate(ary):
        if n >= val:
            return idx 
    return len(ary)