def is_even(n):
    return [False, True][bin(n).endswith("0")]