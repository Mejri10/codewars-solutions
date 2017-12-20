from operator import mul

def isnum(n):
    try:
        int(n)
        return True
    except ValueError:
        return False        

def check_root(string):
    s = string.split(',')
    if len(s) != 4 or not all(map(isnum, s)):
        return 'incorrect input'
    else:
        s = map(int, s)
        if sum(s) != sum(range(s[0], s[-1]+1)):
            return 'not consecutive'
        else:
            n = reduce(mul, s) + 1
            return "{}, {}".format(n, int(n**.5))
            