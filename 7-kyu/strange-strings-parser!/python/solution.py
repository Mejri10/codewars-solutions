import re

def word_splitter(string1):
    return re.split("[^\w.\-]", string1)