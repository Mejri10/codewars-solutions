from math import ceil

def center(strng, width, fill=' '):
    return strng.center(width, fill) if (width - len(strng))%2 == 0 or width-len(strng)<0 else fill + strng.center(width-1, fill)
