import re

def is_digit(n):
    if len(n) > 1: return False
    return re.search(r"^[0-9]$", n) is not None 

