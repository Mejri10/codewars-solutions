def decode(string):
    decoder = dict(zip("0123456789", "5987604321"))
    return ''.join(decoder[d] for d in string)