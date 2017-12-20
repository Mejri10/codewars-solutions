def equalize(arr):
    level = arr[0] if len(arr) > 1 else 0
    return ["+{}".format(n-level) if n-level >= 0 else str(n-level) for n in arr]