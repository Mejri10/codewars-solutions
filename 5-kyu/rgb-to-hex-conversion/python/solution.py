def rgb(r, g, b):
    return ''.join(hex(255 if color > 255 else 0 if color < 0 else color)[2:].zfill(2).upper() for color in (r, g, b))