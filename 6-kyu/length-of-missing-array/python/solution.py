def get_length_of_missing_array(arr):
    if None in arr or not arr: return 0
    lengths = list(map(len, arr))
    return sum(range(min(lengths), max(lengths)+1)) - sum(lengths) if 0 not in lengths else 0
    