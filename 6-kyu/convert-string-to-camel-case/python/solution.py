import re

def to_camel_case(text):
    text = re.split("[-_]", text)
    return ''.join(s.title() if i > 0 else s for i, s in enumerate(text))