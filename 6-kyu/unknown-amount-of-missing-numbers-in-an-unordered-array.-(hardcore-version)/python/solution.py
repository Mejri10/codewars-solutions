def miss_nums_finder(arr):
    maxValue = max(arr)
    completeSet = set(range(1, maxValue + 1))
    currentSet = set(arr)
    return sorted(list(completeSet.difference(currentSet)))