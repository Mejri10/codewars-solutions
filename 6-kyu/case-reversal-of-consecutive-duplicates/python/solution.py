def reverse(s):
    res = ''
    idx = 0
    while idx < len(s):
        id0 = idx
        while idx < len(s)-1 and s[idx] == s[idx+1]:
            idx += 1
        res += s[id0: idx+1].swapcase() if idx - id0 > 0 else s[id0: idx+1]
        idx += 1
    return res
    