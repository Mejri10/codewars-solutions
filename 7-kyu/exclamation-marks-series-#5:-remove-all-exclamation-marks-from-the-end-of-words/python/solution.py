def remove(s):
    return ' '.join(w.rstrip('!') if any(c.isalpha() for c in w) else w for w in s.split())