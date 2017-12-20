from math import ceil

def find_next_power(val, pow_):
    return ceil(val**(1.0/pow_))**pow_    