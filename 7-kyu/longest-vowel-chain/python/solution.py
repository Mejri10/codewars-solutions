import re

def solve(s):
    return max(map(len, re.findall(r"[aeiou]+", s)))