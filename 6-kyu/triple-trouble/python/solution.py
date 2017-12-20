import re

def triple_double(num1, num2):
    tripleMatch = re.search(r"(\d)\1{2}", str(num1))
    if tripleMatch is None:
        return False
    else:
        tripleNum = tripleMatch.group(1)
        return bool(re.search(r"([%s])\1" % tripleNum, str(num2)))


