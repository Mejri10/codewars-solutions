import re

def count_me(data):
    if data.isnumeric():
        match = re.findall("0+|1+|2+|3+|4+|5+|6+|7+|8+|9+", data)
        res = ''
        for s in match:
            res += str(len(s)) + s[0]
        return res
    else:
        return ''