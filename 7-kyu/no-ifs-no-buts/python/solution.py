def no_ifs_no_buts(a, b):
    isSmaller, isGreater, isEqual = a<b, a>b, a==b
    smaller = "{} is smaller than {}".format(a, b)
    greater = "{} is greater than {}".format(a, b)
    equal = "{} is equal to {}".format(a, b)
    return smaller*isSmaller + greater*isGreater + equal*isEqual