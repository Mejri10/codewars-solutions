def find_even_index(arr):
    res = -1
    arr1 = [0] + arr + [0]
    for i in range(1, len(arr1)-1):
        if sum(arr1[:i]) == sum(arr1[i+1:]):
            res = i - 1
            break
    return res
        