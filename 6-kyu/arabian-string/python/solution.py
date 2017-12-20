import re

def camelize(str_):
    str_ = re.findall(r"[a-z0-9]+", str_, re.I)
    return ''.join(s[0].upper() + s[1:].lower() for s in str_)