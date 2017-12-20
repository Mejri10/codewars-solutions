def capitalize(s, ind):
    string = ''
    for i in range(len(s)):
        if i in set(ind):
            string += s[i].upper()
        else:
            string += s[i]
    return string
    