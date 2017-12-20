def cube_odd(arr):
    if any(not isinstance(i, int) for i in arr): return None
    return sum(i**3 for i in arr if i**3 % 2 == 1)