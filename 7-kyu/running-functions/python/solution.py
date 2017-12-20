from functools import reduce

def running(lst, fn):
    res = [lst[0]]
    def my_fn(x, y):
        res.append(fn(x, y))
        return fn(x, y)        
    reduce(my_fn, lst)
    return res
    