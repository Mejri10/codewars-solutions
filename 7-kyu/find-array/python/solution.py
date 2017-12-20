def find_array(arr1, arr2):
    res = []
    for idx in arr2:
        try:
            res.append(arr1[idx])
        except IndexError:
            pass
    return res