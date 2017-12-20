def remove(s):
    res = ''
    for i in range(len(s)):
        if s[i] != '!' or set(s[i:]) == {'!'}:
            res += s[i]
    return res