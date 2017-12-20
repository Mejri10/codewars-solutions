import re

def format_num(n):
    return "{}".format(int(n) + 1).zfill(len(n)) if n else '1'

def increment_string(strng):
    return re.sub("\d*$", lambda m: format_num(m.group(0)) , strng)

