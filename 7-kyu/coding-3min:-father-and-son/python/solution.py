def sc(s):
    s,scopy = list(s),list(s)
    for letter in scopy:
        if not(letter.lower() in scopy and letter.upper() in scopy):
            s.remove(letter)
    return ''.join(s)
        