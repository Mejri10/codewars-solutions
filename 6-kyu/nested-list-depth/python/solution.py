def list_depth(l):
    nest = 1
    while filter(lambda x: isinstance(x,list), l):
        l = filter(lambda x: isinstance(x,list), l)
        l = reduce(lambda x, y: x + y, l)
        nest += 1
    return nest