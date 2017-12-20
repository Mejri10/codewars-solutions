def iq_test(numbers):
    arr = [i % 2 == 0 for i in [int(j) for j in numbers.split()]] 
    if arr.count(True) > 1:
        return arr.index(False)+1
    else:
        return arr.index(True)+1