def find_longest(arr):
    return sorted(arr, key=lambda x: len(str(x)), reverse=True)[0]