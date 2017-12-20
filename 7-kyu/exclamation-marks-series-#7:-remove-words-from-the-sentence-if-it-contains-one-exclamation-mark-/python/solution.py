def remove(s):
    return ' '.join(w for w in s.split() if not list(w).count('!') == 1)