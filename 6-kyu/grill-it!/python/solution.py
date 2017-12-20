def grille(msg, code):
    binary_mask = bin(code)[2:].zfill(len(msg))
    return "".join([letter for i, letter in enumerate(msg) if binary_mask[-len(msg):][i] == "1"])