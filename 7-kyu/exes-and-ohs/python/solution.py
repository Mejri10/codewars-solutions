def xo(s):
    x_count = 0
    o_count = 0
    for letter in s.lower():
        if letter == 'x':
            x_count += 1
        elif letter == 'o':
            o_count += 1
    if x_count == o_count:
        return True
    else:
        return False