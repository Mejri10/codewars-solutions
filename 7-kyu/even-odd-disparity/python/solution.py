def solve(a):
    evens = [x for x in a if isinstance(x, int) and x % 2 == 0]
    odds = [x for x in a if isinstance(x, int) and x % 2 != 0]
    return len(evens) - len(odds)