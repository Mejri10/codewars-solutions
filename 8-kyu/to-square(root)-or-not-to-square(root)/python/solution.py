def square_or_square_root(arr):
    return [(n**.5) if (n**.5).is_integer() else n**2 for n in arr]