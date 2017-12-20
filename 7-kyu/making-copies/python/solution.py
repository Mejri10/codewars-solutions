def copy_list(l):
    if not isinstance(l,list):
        raise TypeError
    return l[::]