def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def sequence_classifier(arr):
    pattern = cmp(arr[1], arr[0])
    total = pattern
    for i in range(1, len(arr) - 1):
        temp = cmp(arr[i+1], arr[i])
        if pattern == -temp and pattern != 0:
            return 0
        total += temp
    if total == (len(arr)-1):
        return 1
    elif total > 0 and total < (len(arr)-1):
        return 2
    elif total == -(len(arr)-1):
        return 3
    elif total < 0 and total > -(len(arr)-1):
        return 4
    else:
        return 5
        