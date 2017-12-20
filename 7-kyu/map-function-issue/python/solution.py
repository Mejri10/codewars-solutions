def func(n):
    return int(n) % 2 == 0    

def map(arr, somefunction):
    if not callable(somefunction):
        return 'given argument is not a function'
    elif any(str(n).isalpha() for n in arr):
        return 'array should contain only numbers'
    else:
        return [somefunction(n) for n in arr]