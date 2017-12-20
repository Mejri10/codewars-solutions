import re

def err(s):
    vowels = 'aeiouAEIOU'
    if s[-1] not in vowels:
        if s[-1].islower():
            return s + 'err'
        else:
            return s + 'ERR'
    else:
        return s
    
def err_bob(string):
    return re.sub('\w+', lambda m: err(m.group(0)), string)
    