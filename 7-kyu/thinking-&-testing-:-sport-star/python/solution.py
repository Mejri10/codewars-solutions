def testit(act, s):
    t = zip(act, s)
    res = ''
    for i in t:
        if i == ('run', '_'):
            res += '_'
        elif i == ('run', '|'):
            res += '/'
        elif i == ('jump', '_'):
            res += 'x'
        else:
            res += '|'
    return res
        