def pig_it(text):
    return ' '.join(s[1:] + s[0] + 'ay' if s.isalpha() else s for s in text.split())