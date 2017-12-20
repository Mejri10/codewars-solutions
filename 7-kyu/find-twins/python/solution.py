def elimination(arr):
    criminals = [i for i in arr if arr.count(i) > 1]
    return criminals[0] if criminals else None