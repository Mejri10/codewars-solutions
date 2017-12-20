preffixes = {0:  '' , 3:  'k', 6:  'M',
             9:  'G', 12: 'T', 15: 'P',
             18: 'E', 21: 'Z', 24: 'Y'}

def meters(x):
    exponent = 3 * (int("{:e}".format(x).split('+')[1])//3)
    mantissa = str(x/10**exponent).rstrip('0').rstrip('.')
    return "{}{}m".format(mantissa, preffixes[exponent])