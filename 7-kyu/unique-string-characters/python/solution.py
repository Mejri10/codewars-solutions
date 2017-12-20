def solve(a,b):
    ans = ""
    charSet = set(a).symmetric_difference(set(b))
    for c in (a + b):
        if c in charSet:
            ans += c
    return ans
    