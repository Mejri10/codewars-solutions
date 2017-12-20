import re

def reverse_words(s):
    return re.sub(r'[^\s]+', lambda m: m.group(0)[::-1], s)