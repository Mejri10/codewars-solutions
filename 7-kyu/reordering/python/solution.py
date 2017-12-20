def re_ordering(text):
    return ' '.join(sorted(text.split(), key=lambda x: 0 if x[0].isupper() else 1))
