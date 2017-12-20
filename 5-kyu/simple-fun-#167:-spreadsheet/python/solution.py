import re


def spreadsheet(s):
    if s.startswith('R'):
        r, c = re.findall(r"[0-9]+", s)
        c = int(c)
        res = ''
        while c >= 1:
            c -= 1
            res = chr(65 + (c % 26)) + res
            c = c // 26
        return "{}{}".format(res, r)                
    else:
        c, r = re.findall(r"[A-Z]+|[0-9]+", s)
        return "R{}C{}".format(r, str(sum(26**idx * (ord(letter) - 64) for idx, letter in enumerate(c[::-1]))))