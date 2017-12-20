def find_uniq(arr):
    arr2 = [''.join(list(set(sorted(n.strip().lower())))) for n in arr]
    setarr2 = set( _ for _ in arr2) 
    for n in setarr2:
        if arr2.count(n) == 1:
            return arr[arr2.index(n)]