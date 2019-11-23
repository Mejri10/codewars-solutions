def rankings(arr):
    arr_sorted = sorted(arr, reverse=True)
    return [arr_sorted.index(n) + 1 for n in arr]