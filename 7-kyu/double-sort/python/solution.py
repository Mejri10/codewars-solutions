def db_sort(arr): 
    strings = filter(lambda n: isinstance(n, str), arr)
    nums = filter(lambda n: isinstance(n, int), arr)
    return sorted(nums) + sorted(strings)