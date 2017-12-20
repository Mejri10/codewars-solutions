from fractions import gcd

def mixed_fraction(s):
    num, den = map(abs, map(int, s.split('/')))
    if den == 0:
        raise ZeroDivisionError
    whole, num = divmod(num, den)
    factor = gcd(num, den)
    num /= factor
    den /= factor
    isnegative = s.count('-') % 2
    if whole == 0 and num == 0:
        return '0'
    elif whole == 0:    
        return '-'*isnegative + "%d/%d" % (num, den) 
    elif num == 0:
        return '-'*isnegative + "%d" % whole
    else:
        return '-'*isnegative + "%d %d/%d" % (whole, num, den)