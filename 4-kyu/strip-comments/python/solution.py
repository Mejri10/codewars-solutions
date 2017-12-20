import re

def solution(string, markers):
    escape_chars = "-^"
    if not markers:
        return string
    else:
        markers = ''.join("\\" + ch if ch in escape_chars else ch for ch in markers)
        regex = r"[ ]*?[{}].*(\n?)".format(markers)
        return re.sub(regex, lambda x: x.group(1), string)