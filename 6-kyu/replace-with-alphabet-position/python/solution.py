from re import sub

def alphabet_position(text):
    return ' '.join([str(ord(c) - 96) for c in sub(r"[^a-z]", "", text.lower())])