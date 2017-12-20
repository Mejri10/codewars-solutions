def find_deleted_number(arr, mixed_arr):
    difference = set(arr).difference(set(mixed_arr))
    return list(difference)[0] if difference else 0