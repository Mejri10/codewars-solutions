def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    set1 = set(array1)
    set1Squared = set([n * n for n in array1])
    set2 = set(array2)
    return set1Squared == set2
    
	